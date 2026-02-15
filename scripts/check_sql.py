"""Execute the journal check against valid, imbalanced, and missing fixtures."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from fintech_lab.warehouse import connect,ingest
from fintech_lab.synthetic import payments

query=(ROOT/'sql/solutions/05-ledger.sql').read_text(encoding='utf-8')
db=connect()
try:
    ingest(db,payments())
    assert [tuple(r) for r in db.execute(query)]==[]
    db.execute("UPDATE ledger_entries SET signed_minor=signed_minor+1 WHERE event_id='e1' AND account='processor_receivable'")
    assert [tuple(r) for r in db.execute(query)]==[('e1','USD')]
    db.rollback()
    db.execute("DELETE FROM ledger_entries WHERE event_id='e2'")
    assert [tuple(r) for r in db.execute(query)]==[('e2','USD')]
    print('SQL check passed: valid, imbalance and entirely missing journal')
finally:
    db.close()
