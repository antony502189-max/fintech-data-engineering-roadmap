def solve(data):
    import sqlite3
    db=sqlite3.connect(':memory:')
    db.execute('CREATE TABLE events(event_id TEXT,payment_id TEXT,kind TEXT,amount INTEGER,currency TEXT,seq INTEGER)')
    db.executemany('INSERT INTO events VALUES(?,?,?,?,?,?)', data['events'])
    try:
        return [list(r) for r in db.execute('SELECT event_id,count(*) FROM events GROUP BY event_id HAVING count(*)>1 ORDER BY event_id')]
    finally:
        db.close()
