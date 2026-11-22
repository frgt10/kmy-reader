import unittest
import xml.etree.ElementTree as elementTree
from datetime import date
from decimal import Decimal
from pathlib import Path

from kmy.kmy import Kmy
from kmy.split import Split

file_name = Path(__file__).parent / "Test.kmy"


class TestSplit(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.splits = mm.transactions[0].splits
        self.split0 = self.splits[0]

    def test_read_splits_count(self):
        self.assertEqual(2, len(self.splits))

    def test_read_payee(self):
        self.assertEqual('', self.split0.payee)

    def test_read_memo(self):
        self.assertEqual('', self.split0.memo)

    def test_read_shares(self):
        self.assertEqual(Decimal("42"), self.split0.shares)

    def test_read_number(self):
        self.assertEqual('', self.split0.number)

    def test_read_action(self):
        self.assertEqual('', self.split0.action)

    def test_read_price(self):
        self.assertEqual(Decimal("1"), self.split0.price)

    def test_read_account(self):
        self.assertEqual('A000001', self.split0.account)

    def test_read_reconcileflag(self):
        self.assertEqual('0', self.split0.reconcileFlag)

    def test_read_bankid(self):
        self.assertEqual('', self.split0.bankId)

    def test_read_value(self):
        self.assertEqual(Decimal("42"), self.split0.value)

    def test_read_reconciledate(self):
        self.assertIsNone(self.split0.reconcileDate)

    def test_read_reconciledate_value(self):
        node = elementTree.fromstring(
            '<SPLIT payee="" memo="" shares="1/1" number="" action="" price="1/1" '
            'account="" reconcileflag="1" bankid="" value="1/1" '
            'reconciledate="2024-05-06" id="S0002"/>'
        )
        self.assertEqual(date(2024, 5, 6), Split.from_xml(node).reconcileDate)

    def test_read_id(self):
        self.assertEqual('S0001', self.split0.id)

    def test_read_fractional_values_as_decimal(self):
        node = elementTree.fromstring(
            '<SPLIT payee="" memo="" shares="3/2" number="" action="" price="1/4" '
            'account="" reconcileflag="0" bankid="" value="-100/100" '
            'reconciledate="" id="S0001"/>'
        )
        split = Split.from_xml(node)
        self.assertEqual(Decimal("1.5"), split.shares)
        self.assertEqual(Decimal("0.25"), split.price)
        self.assertEqual(Decimal("-1"), split.value)


if __name__ == '__main__':
    unittest.main()
