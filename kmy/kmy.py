import gzip
import xml.etree.ElementTree as elementTree
from typing import Dict
from typing import List
from typing import Optional

from .account import Account
from .costcenter import CostCenter
from .fileinfo import FileInfo
from .institution import Institution
from .pairs import pairs_dict_from_xml
from .payee import Payee
from .tag import Tag
from .transaction import Transaction
from .user import User


class Kmy:
    def __init__(
        self,
        fileInfo: Optional[FileInfo] = None,
        user: Optional[User] = None,
        institutions: Optional[List[Institution]] = None,
        payees: Optional[List[Payee]] = None,
        costCenters: Optional[List[CostCenter]] = None,
        tags: Optional[List[Tag]] = None,
        accounts: Optional[List[Account]] = None,
        transactions: Optional[List[Transaction]] = None,
        keyValuePairs: Optional[Dict[str, str]] = None,
    ):
        self.fileInfo = fileInfo if fileInfo is not None else FileInfo()
        self.user = user if user is not None else User()
        self.institutions = institutions if institutions is not None else []
        self.payees = payees if payees is not None else []
        self.costCenters = costCenters if costCenters is not None else []
        self.tags = tags if tags is not None else []
        self.accounts = accounts if accounts is not None else []
        self.transactions = transactions if transactions is not None else []
        self.keyValuePairs = keyValuePairs if keyValuePairs is not None else {}

    def __repr__(self):
        return f"{self.__class__.__name__}(fileInfo='{self.fileInfo}', user={self.user})"

    @classmethod
    def from_xml(cls, node):
        return cls(
            fileInfo=FileInfo.from_xml(node.find("FILEINFO")),
            user=User.from_xml(node.find("USER")),
            institutions=[
                Institution.from_xml(institution_node)
                for institution_node in node.find("INSTITUTIONS")
            ],
            payees=[
                Payee.from_xml(payee_node) for payee_node in node.find("PAYEES")
            ],
            costCenters=[
                CostCenter.from_xml(costcenter_node)
                for costcenter_node in node.find("COSTCENTERS")
            ],
            tags=[Tag.from_xml(tag_node) for tag_node in node.find("TAGS")],
            accounts=[
                Account.from_xml(account_node) for account_node in node.find("ACCOUNTS")
            ],
            transactions=[
                Transaction.from_xml(transaction_node)
                for transaction_node in node.find("TRANSACTIONS")
            ],
            keyValuePairs=pairs_dict_from_xml(node.find("KEYVALUEPAIRS")),
        )

    @classmethod
    def from_kmy_file(cls, file_name):
        file_open = gzip.open if is_gz_file(file_name) else open
        with file_open(file_name, 'rb') as file:
            tree = elementTree.parse(file)
        root = tree.getroot()
        kmm = Kmy.from_xml(root)
        return kmm


def is_gz_file(filepath):
    with open(filepath, 'rb') as test_f:
        return test_f.read(2) == b'\x1f\x8b'
