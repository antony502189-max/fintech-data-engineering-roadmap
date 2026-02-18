import unittest
from fintech_lab.money import to_minor

class MoneyTests(unittest.TestCase):
    def test_exact_usd(self):
        self.assertEqual(to_minor("10.01", "USD"), 1001)
    def test_jpy(self):
        self.assertEqual(to_minor("100", "JPY"), 100)
    def test_kwd(self):
        self.assertEqual(to_minor("1.234", "KWD"), 1234)
    def test_precision_rejected(self):
        for amount,currency in [("1.001", "USD"), ("1.2", "JPY")]:
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                to_minor(amount,currency)
    def test_float_rejected(self):
        with self.assertRaises(TypeError): to_minor(0.1,"USD")
    def test_nonfinite_rejected(self):
        for amount in ("NaN", "Infinity", "-Infinity", "wrong"):
            with self.subTest(amount=amount), self.assertRaises(ValueError): to_minor(amount,"USD")
    def test_currency_rejected(self):
        with self.assertRaises(ValueError): to_minor("1","XXX")
    def test_negative_is_exact(self):
        self.assertEqual(to_minor("-1.23","USD"),-123)
    def test_bound(self):
        with self.assertRaises(ValueError): to_minor("99999999999999999999","USD")
    def test_precision_beyond_default_decimal_context(self):
        with self.assertRaises(ValueError): to_minor("1.00000000000000000000000000001","USD")
    def test_large_exponent_rejected_without_integer_expansion(self):
        for amount in ("1e10000", "1e1000000", "1e-1000000"):
            with self.subTest(amount=amount), self.assertRaises(ValueError): to_minor(amount,"USD")
    def test_zero_with_extreme_exponent(self):
        self.assertEqual(to_minor("0e1000000","USD"),0)
