"""Late dimension versions and historical facts, with an actual temporal SQL join."""
from fintech_lab.warehouse import connect
from fintech_lab.scd import apply_change
from fintech_lab.contracts import parse_time

def solve(data):
    db = connect()
    try:
        for change in data['changes']:
            try:
                apply_change(db, change['customer'], change['tier'], change['effective_at'])
            except ValueError:
                return {'status': 'conflict'}
        db.execute('CREATE TABLE facts(id TEXT PRIMARY KEY, customer TEXT, at TEXT, amount INTEGER, currency TEXT)')
        db.executemany('INSERT INTO facts VALUES(?,?,?,?,?)', [
            (r['id'], r['customer'], parse_time(r['at']).isoformat(), r['amount'], r['currency'])
            for r in data['facts']])
        db.execute('''CREATE VIEW joined AS
            SELECT f.id,coalesce(h.tier,'UNKNOWN') AS tier,f.amount,f.currency
            FROM facts f LEFT JOIN customers_history h
              ON f.customer=h.customer_id AND h.valid_from<=f.at
             AND (h.valid_to IS NULL OR f.at<h.valid_to)''')
        return {
            'facts': [dict(r) for r in db.execute('SELECT * FROM joined ORDER BY id')],
            'totals': [dict(r) for r in db.execute('''SELECT tier,currency,sum(amount) AS amount
                FROM joined GROUP BY tier,currency ORDER BY tier,currency''')],
        }
    finally:
        db.close()
