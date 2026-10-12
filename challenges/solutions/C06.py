"""Restore a real SQLite backup and replay with an atomic data/checkpoint boundary."""
import sqlite3

class InjectedCrash(RuntimeError):
    pass

def state(db):
    return {'checkpoint': db.execute('SELECT value FROM checkpoint').fetchone()[0],
            'ids': [r[0] for r in db.execute('SELECT id FROM events ORDER BY id')],
            'total_minor': db.execute('SELECT coalesce(sum(amount),0) FROM events').fetchone()[0]}

def apply(db, batch, crash=False):
    if batch['end_seq'] <= state(db)['checkpoint']:
        return 'skipped'
    with db:
        for identity, amount in batch['events']:
            old = db.execute('SELECT amount FROM events WHERE id=?', (identity,)).fetchone()
            if old:
                if old[0] != amount:
                    raise ValueError('Identity conflict')
            else:
                db.execute('INSERT INTO events VALUES(?,?)', (identity, amount))
        if crash:
            raise InjectedCrash('Failure after data, before checkpoint')
        db.execute('UPDATE checkpoint SET value=?', (batch['end_seq'],))
    return 'committed'

def solve(data):
    live, backup, restored = [sqlite3.connect(':memory:') for _ in range(3)]
    try:
        live.executescript('''CREATE TABLE events(id TEXT PRIMARY KEY,amount INTEGER);
            CREATE TABLE checkpoint(value INTEGER); INSERT INTO checkpoint VALUES(0);''')
        live.commit()
        live.backup(backup)
        trace = []
        for number, batch in enumerate(data['batches'], 1):
            blocked = False
            attempts = 2 if batch.get('crash_before_checkpoint', False) else 1
            for attempt in range(1, attempts+1):
                try:
                    status = apply(live, batch, crash=attempt == 1 and attempts == 2)
                except InjectedCrash:
                    status = 'rolled_back'
                except ValueError:
                    status = 'conflict'; blocked = True
                trace.append({'batch': number, 'attempt': attempt, 'status': status, **state(live)})
                if blocked or status != 'rolled_back':
                    break
            if number == data['backup_after']:
                live.backup(backup)
            if blocked:
                break
        backup.backup(restored)
        for batch in data['batches']:
            try:
                apply(restored, batch)
            except ValueError:
                break
        current, recovered = state(live), state(restored)
        return {'attempts': trace, 'live': current, 'restored': recovered, 'equal': current == recovered}
    finally:
        for db in (live, backup, restored):
            db.close()
