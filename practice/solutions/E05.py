def solve(data):
    import sqlite3
    db=sqlite3.connect(':memory:')
    db.execute('CREATE TABLE events(event_id TEXT,payment_id TEXT,kind TEXT,amount INTEGER,currency TEXT,seq INTEGER)')
    db.executemany('INSERT INTO events VALUES(?,?,?,?,?,?)', data['events'])
    try:
        return [list(r) for r in db.execute('SELECT count(*),count(DISTINCT payment_id) FROM events')]
    finally:
        db.close()
