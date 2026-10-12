"""Query both validity and knowledge intervals, and expose overlapping matches."""
import sqlite3
from fintech_lab.contracts import parse_time

def solve(data):
    db = sqlite3.connect(':memory:')
    try:
        db.execute('CREATE TABLE history(entity TEXT,value TEXT,vf TEXT,vt TEXT,rf TEXT,rt TEXT)')
        stamp = lambda value: None if value is None else parse_time(value).isoformat()
        db.executemany('INSERT INTO history VALUES(?,?,?,?,?,?)', [
            (r['entity'], r['value'], stamp(r['valid_from']), stamp(r['valid_to']),
             stamp(r['recorded_from']), stamp(r['recorded_to'])) for r in data['records']])
        result = []
        for query in data['queries']:
            business, known = stamp(query['business_at']), stamp(query['known_at'])
            values = db.execute('''SELECT value FROM history WHERE entity=?
                AND vf<=? AND (vt IS NULL OR ?<vt)
                AND rf<=? AND (rt IS NULL OR ?<rt)''',
                (query['entity'], business, business, known, known)).fetchall()
            if len(values)>1:
                result.append({'id': query['id'], 'error': 'overlap'})
            else:
                result.append({'id': query['id'], 'value': values[0][0] if values else None})
        return result
    finally:
        db.close()
