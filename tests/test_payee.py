import unittest
import xml.etree.ElementTree as elementTree
from pathlib import Path

from kmy.kmy import Kmy
from kmy.payee import Payee

file_name = Path(__file__).parent / "Test.kmy"


class TestPayee(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.payees = mm.payees
        self.payee0 = self.payees[0]

    def test_read_payees_count(self):
        self.assertEqual(3, len(self.payees))

    def test_read_reference(self):
        self.assertEqual("", self.payee0.reference)

    def test_read_name(self):
        self.assertEqual("Some From", self.payee0.name)

    def test_read_email(self):
        self.assertEqual("who@ville.tld", self.payee0.email)

    def test_read_id(self):
        self.assertEqual("P000001", self.payee0.id)

    def test_read_matching_enabled(self):
        self.assertEqual(False, self.payee0.matchingEnabled)

    def test_read_matchkeys_default(self):
        self.assertEqual([], Payee().matchkeys)

    def test_read_matchkey(self):
        node = elementTree.fromstring(
            '<PAYEE reference="" name="Some From" email="" id="P000001" '
            'matchingenabled="1" usingmatchkey="1" matchkey="^Foo$"/>'
        )
        self.assertEqual(["^Foo$"], Payee.from_xml(node).matchkeys)

    def test_read_missing_matchkey(self):
        node = elementTree.fromstring(
            '<PAYEE reference="" name="Some From" email="" id="P000001" '
            'matchingenabled="0"/>'
        )
        self.assertEqual([], Payee.from_xml(node).matchkeys)


if __name__ == "__main__":
    unittest.main()
