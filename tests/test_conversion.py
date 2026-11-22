import unittest
from decimal import Decimal

from kmy.conversion import fraction_to_decimal


class TestFractionToDecimal(unittest.TestCase):
    def test_integer_fraction(self):
        self.assertEqual(Decimal("42"), fraction_to_decimal("42/1"))

    def test_fractional_value(self):
        self.assertEqual(Decimal("1.5"), fraction_to_decimal("3/2"))

    def test_negative_value(self):
        self.assertEqual(Decimal("-1"), fraction_to_decimal("-100/100"))

    def test_empty_value(self):
        self.assertEqual(Decimal(0), fraction_to_decimal(""))


if __name__ == "__main__":
    unittest.main()
