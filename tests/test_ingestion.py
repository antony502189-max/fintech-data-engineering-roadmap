import unittest
from fintech_lab.warehouse import connect, ingest, daily, assert_balanced, ConflictingEvent
from fintech_lab.synthetic import payments, event

class IngestionTests(unittest.TestCase):
    def setUp(self): self.db = connect()
    def tearDown(self): self.db.close()
    def test_replay_is_idempotent(self):
        self.assertEqual(ingest(self.db,payments())["inserted"],6)
        before=daily(self.db)
        self.assertEqual(ingest(self.db,payments())["duplicates"],6)
        self.assertEqual(before,daily(self.db))
        self.assertEqual(self.db.execute("SELECT count(*) FROM ledger_entries").fetchone()[0],12)
    def test_new_delivery_time_is_duplicate(self):
        original=payments()[0]
        ingest(self.db,[original])
        retry=dict(original,received_at="2026-01-05T00:00:00Z")
        self.assertEqual(ingest(self.db,[retry])["duplicates"],1)
    def test_conflict_rolls_back_batch(self):
        original=payments()[0]
        ingest(self.db,[original])
        with self.assertRaises(ConflictingEvent):
            ingest(self.db,[event("new","new","captured",100),dict(original,amount_minor=10001)])
        self.assertEqual(self.db.execute("SELECT count(*) FROM raw_events").fetchone()[0],1)
    def test_invalid_is_quarantined(self):
        self.assertEqual(ingest(self.db,[dict(payments()[0],amount_minor=True)])["quarantined"],1)
        self.assertEqual(self.db.execute("SELECT count(*) FROM ledger_entries").fetchone()[0],0)
    def test_missing_field(self):
        bad=payments()[0]; del bad["currency"]
        self.assertEqual(ingest(self.db,[bad])["quarantined"],1)
    def test_extra_field(self):
        self.assertEqual(ingest(self.db,[dict(payments()[0],pan="SYNTHETIC")])["quarantined"],1)
    def test_ledger_balanced(self):
        ingest(self.db,payments()); assert_balanced(self.db)
    def test_broken_posting_detected(self):
        ingest(self.db,payments())
        self.db.execute("UPDATE ledger_entries SET signed_minor=signed_minor+1 WHERE event_id='e1' AND account='processor_receivable'")
        with self.assertRaises(AssertionError): assert_balanced(self.db)
    def test_missing_journal_detected(self):
        ingest(self.db,payments())
        self.db.execute("DELETE FROM ledger_entries WHERE event_id='e1'")
        with self.assertRaises(AssertionError): assert_balanced(self.db)
    def test_currency_grain(self):
        ingest(self.db,payments())
        rows={(r["event_date"],r["currency"]):r["net_minor"] for r in daily(self.db)}
        self.assertEqual(rows, {("2026-01-01","USD"):12200,("2026-01-01","EUR"):4900,("2026-01-02","USD"):-2000})
    def test_bad_datetime(self):
        for stamp in ("2026-01-01T12:00:00", "garbage"):
            with self.subTest(stamp=stamp):
                self.assertEqual(ingest(self.db,[dict(payments()[0],event_time=stamp)])["quarantined"],1)
    def test_normalized_offsets(self):
        row=dict(payments()[0],event_time="2026-01-01T15:00:00+03:00")
        ingest(self.db,[row])
        self.assertEqual(ingest(self.db,[payments()[0]])["duplicates"],1)
    def test_delivery_before_event(self):
        self.assertEqual(ingest(self.db,[dict(payments()[0],received_at="2025-12-31T00:00:00Z")])["quarantined"],1)
