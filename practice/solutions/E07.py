def solve(data):
    import sqlite3
    db=sqlite3.connect(':memory:')
    db.execute('CREATE TABLE events(event_id TEXT,payment_id TEXT,kind TEXT,amount INTEGER,currency TEXT,seq INTEGER)')
    db.executemany('INSERT INTO events VALUES(?,?,?,?,?,?)', data['events'])
    try:
        return [list(r) for r in db.execute('SELECT payment_id,kind FROM (SELECT *,row_number() OVER(PARTITION BY payment_id ORDER BY seq DESC,event_id DESC) AS rn FROM events) WHERE rn=1 ORDER BY payment_id')]
    finally:
        db.close()
