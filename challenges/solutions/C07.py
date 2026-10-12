"""Repair fanout using independent aggregates, retaining zero-fee payments."""
import sqlite3

def solve(data):
    db = sqlite3.connect(':memory:')
    try:
        db.executescript('''CREATE TABLE captures(id TEXT,payment TEXT,currency TEXT,amount INTEGER);
            CREATE TABLE fees(id TEXT,payment TEXT,currency TEXT,amount INTEGER);
            CREATE TABLE attempts(id TEXT,payment TEXT);''')
        db.executemany('INSERT INTO captures VALUES(?,?,?,?)', data['captures'])
        db.executemany('INSERT INTO fees VALUES(?,?,?,?)', data['fees'])
        db.executemany('INSERT INTO attempts VALUES(?,?)', data['attempts'])
        query = '''WITH c AS (SELECT payment,currency,sum(amount) gross
                     FROM captures GROUP BY payment,currency),
            f AS (SELECT payment,currency,sum(amount) fee FROM fees GROUP BY payment,currency),
            a AS (SELECT payment,count(*) attempts FROM attempts GROUP BY payment)
            SELECT c.payment,c.currency,c.gross,c.gross-coalesce(f.fee,0),coalesce(a.attempts,0)
            FROM c LEFT JOIN f ON c.payment=f.payment AND c.currency=f.currency
            LEFT JOIN a ON c.payment=a.payment ORDER BY c.payment,c.currency'''
        return [list(row) for row in db.execute(query)]
    finally:
        db.close()
