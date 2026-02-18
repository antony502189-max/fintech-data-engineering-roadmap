import unittest
from fintech_lab.warehouse import connect, ingest
from fintech_lab.synthetic import payments, settlement
from fintech_lab.reconcile import reconcile

class ReconciliationTests(unittest.TestCase):
    def setUp(self): self.db=connect(); ingest(self.db,payments())
    def tearDown(self): self.db.close()
    def test_matched(self):
        report=reconcile(self.db,settlement())
        self.assertEqual(report[0]["status"],"matched")
        self.assertEqual(report[1]["status"],"matched")
    def test_mismatch(self):
        row=reconcile(self.db,settlement())[2]
        self.assertEqual((row["status"],row["delta_minor"]),("amount_mismatch",-100))
    def test_unexpected(self):
        row=reconcile(self.db,settlement())[3]
        self.assertEqual(row["status"],"unexpected_external")
        self.assertIsNone(row["expected_minor"])
    def test_missing(self):
        self.assertEqual({r["status"] for r in reconcile(self.db,[])},{"missing_external"})
    def test_duplicate_external_fails(self):
        with self.assertRaises(ValueError): reconcile(self.db,[settlement()[0],settlement()[0]])
    def test_float_external_fails(self):
        with self.assertRaises(ValueError): reconcile(self.db,[dict(settlement()[0],net_minor=77.0)])
    def test_currency_cannot_cross_match(self):
        report=reconcile(self.db,[dict(settlement()[0],currency="EUR")])
        p1=[r for r in report if r["payment_id"]=="p1"]
        self.assertEqual({r["status"] for r in p1},{"missing_external","unexpected_external"})
