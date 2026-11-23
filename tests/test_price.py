import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestPrice(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.prices = mm.pricePairs[0].prices
        self.price0 = self.prices[0]

    def test_read_date(self):
        self.assertEqual(date(2020, 12, 13), self.price0.date)

    def test_read_source(self):
        self.assertEqual("KMyMoney", self.price0.source)

    def test_read_price(self):
        self.assertEqual(Decimal("123.45"), self.price0.price)

    def test_read_fractional_price(self):
        self.assertEqual(Decimal("1.5"), self.prices[1].price)


if __name__ == "__main__":
    unittest.main()
