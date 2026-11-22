import unittest
from datetime import date
from decimal import Decimal

from kmy.conversion import fraction_to_decimal
from kmy.conversion import parse_date


class TestFractionToDecimal(unittest.TestCase):
    def test_integer_fraction(self):
        self.assertEqual(Decimal("42"), fraction_to_decimal("42/1"))

    def test_fractional_value(self):
        self.assertEqual(Decimal("1.5"), fraction_to_decimal("3/2"))

    def test_negative_value(self):
        self.assertEqual(Decimal("-1"), fraction_to_decimal("-100/100"))

    def test_empty_value(self):
        self.assertEqual(Decimal(0), fraction_to_decimal(""))

    def test_parse_date(self):
        self.assertEqual(date(2020, 1, 1), parse_date("2020-01-01"))

    def test_parse_datetime_with_offset(self):
        self.assertEqual(
            date(2026, 11, 20),
            parse_date("2026-11-20T22:18:09+03:00"),
        )

    def test_parse_datetime_with_z(self):
        self.assertEqual(date(2020, 1, 1), parse_date("2020-01-01T00:00:00Z"))

    def test_parse_empty_date(self):
        self.assertIsNone(parse_date(""))


if __name__ == "__main__":
    unittest.main()
