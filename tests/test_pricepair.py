import unittest
from pathlib import Path

from kmy.kmy import Kmy

file_name = Path(__file__).parent / "Test.kmy"


class TestPricepair(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.pricePairs = mm.pricePairs
        self.pricePair0 = self.pricePairs[0]

    def test_read_pricepairs_count(self):
        self.assertEqual(2, len(self.pricePairs))

    def test_read_cur_from(self):
        self.assertEqual("USD", self.pricePair0.curFrom)

    def test_read_cur_to(self):
        self.assertEqual("EUR", self.pricePair0.curTo)

    def test_read_prices_count(self):
        self.assertEqual(2, len(self.pricePair0.prices))


if __name__ == "__main__":
    unittest.main()
