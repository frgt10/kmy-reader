import gzip
import xml.etree.ElementTree as elementTree
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from .account import Account
from .costcenter import CostCenter
from .fileinfo import FileInfo
from .institution import Institution
from .pairs import pairs_dict_from_xml
from .payee import Payee
from .pricepair import Pricepair
from .security import Security
from .tag import Tag
from .transaction import Transaction
from .user import User


@dataclass(frozen=True, repr=False)
class Kmy:
    fileInfo: FileInfo = field(default_factory=FileInfo)
    user: User = field(default_factory=User)
    institutions: List[Institution] = field(default_factory=list, compare=False)
    payees: List[Payee] = field(default_factory=list, compare=False)
    costCenters: List[CostCenter] = field(default_factory=list, compare=False)
    tags: List[Tag] = field(default_factory=list, compare=False)
    accounts: List[Account] = field(default_factory=list, compare=False)
    transactions: List[Transaction] = field(default_factory=list, compare=False)
    pricePairs: List[Pricepair] = field(default_factory=list, compare=False)
    securities: List[Security] = field(default_factory=list, compare=False)
    keyValuePairs: Dict[str, str] = field(default_factory=dict, compare=False)

    def __repr__(self):
        return f"{self.__class__.__name__}(fileInfo={self.fileInfo}, user={self.user})"

    @classmethod
    def from_xml(cls, node):
        return cls(
            fileInfo=FileInfo.from_xml(node.find("FILEINFO")),
            user=User.from_xml(node.find("USER")),
            institutions=[
                Institution.from_xml(institution_node)
                for institution_node in node.find("INSTITUTIONS")
            ],
            payees=[Payee.from_xml(payee_node) for payee_node in node.find("PAYEES")],
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
            pricePairs=[
                Pricepair.from_xml(price_pair_node)
                for price_pair_node in node.find("PRICES")
            ],
            securities=[
                Security.from_xml(security_node)
                for security_node in node.find("SECURITIES")
            ],
            keyValuePairs=pairs_dict_from_xml(node.find("KEYVALUEPAIRS")),
        )

    @classmethod
    def from_kmy_file(cls, file_name):
        file_open = gzip.open if is_gz_file(file_name) else open
        with file_open(file_name, "rb") as file:
            tree = elementTree.parse(file)
        root = tree.getroot()
        kmm = Kmy.from_xml(root)
        return kmm


def is_gz_file(filepath):
    with open(filepath, "rb") as test_f:
        return test_f.read(2) == b"\x1f\x8b"
