"""Multi-batch ingestion: preserve accepted state through replay and conflicts."""
from fintech_lab.warehouse import connect, ingest, daily, assert_balanced, ConflictingEvent

def solve(data):
    db = connect()
    try:
        steps = []
        for batch in data['batches']:
            try:
                result = {'status': 'committed', **ingest(db, batch)}
            except ConflictingEvent:
                result = {'status': 'conflict'}
            assert_balanced(db)
            result['daily'] = daily(db)
            steps.append(result)
        return {
            'steps': steps,
            'event_ids': [r[0] for r in db.execute('SELECT event_id FROM raw_events ORDER BY event_id')],
            'posting_count': db.execute('SELECT count(*) FROM ledger_entries').fetchone()[0],
            'quarantine_count': db.execute('SELECT count(*) FROM quarantine').fetchone()[0],
        }
    finally:
        db.close()
