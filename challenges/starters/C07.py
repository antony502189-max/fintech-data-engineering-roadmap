"""Debug this runnable report: passing syntax does not prove monetary correctness."""
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
        # This intentionally broken report runs; find its semantic defects.
        query = '''SELECT c.payment,c.currency,sum(DISTINCT c.amount),
            sum(DISTINCT c.amount)-sum(DISTINCT f.amount),count(a.id)
            FROM captures c JOIN fees f ON c.payment=f.payment
            JOIN attempts a ON c.payment=a.payment
            GROUP BY c.payment,c.currency ORDER BY c.payment,c.currency'''
        return [list(row) for row in db.execute(query)]
    finally:
        db.close()
