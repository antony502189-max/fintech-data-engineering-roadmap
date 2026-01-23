def solve(data):
    import sqlite3
    db=sqlite3.connect(':memory:')
    db.execute('CREATE TABLE events(event_id TEXT,payment_id TEXT,kind TEXT,amount INTEGER,currency TEXT,seq INTEGER)')
    db.executemany('INSERT INTO events VALUES(?,?,?,?,?,?)', data['events'])
    try:
        return [list(r) for r in db.execute("SELECT currency,sum(CASE WHEN kind='captured' THEN amount ELSE -amount END) FROM events GROUP BY currency ORDER BY currency")]
    finally:
        db.close()
