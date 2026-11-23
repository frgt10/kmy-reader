import unittest
from decimal import Decimal
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestSecurity(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.securities = mm.securities
        self.security0 = self.securities[0]
        self.security1 = self.securities[1]

    def test_read_securities_count(self):
        self.assertEqual(2, len(self.securities))

    def test_read_id(self):
        self.assertEqual("E000001", self.security0.id)

    def test_read_symbol(self):
        self.assertEqual("ALP", self.security0.symbol)

    def test_read_name(self):
        self.assertEqual("Alpha Corp", self.security0.name)

    def test_read_saf(self):
        self.assertEqual(1, self.security0.saf)

    def test_read_pp(self):
        self.assertEqual(2, self.security0.pp)

    def test_read_trading_currency(self):
        self.assertEqual("USD", self.security0.tradingCurrency)

    def test_read_trading_market(self):
        self.assertEqual("NASDAQ", self.security0.tradingMarket)

    def test_read_type(self):
        self.assertEqual("0", self.security0.type)

    def test_read_rounding_method(self):
        self.assertEqual("7", self.security0.roundingMethod)

    def test_read_online_factor(self):
        self.assertEqual(Decimal("1.5"), self.security0.onlineFactor)

    def test_read_online_source(self):
        self.assertEqual("Yahoo", self.security0.onlineSource)

    def test_read_security_id(self):
        self.assertEqual("SEC-001", self.security0.securityId)

    def test_read_defaults_without_key_value_pairs(self):
        self.assertEqual(Decimal(1), self.security1.onlineFactor)
        self.assertEqual("", self.security1.onlineSource)
        self.assertEqual("", self.security1.securityId)


if __name__ == "__main__":
    unittest.main()
