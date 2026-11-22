from dataclasses import dataclass
from decimal import Decimal

from .conversion import fraction_to_decimal


@dataclass(frozen=True)
class Split:
    payee: str = ""
    memo: str = ""
    shares: Decimal = Decimal(0)
    number: str = ""
    action: str = ""
    price: Decimal = Decimal(0)
    account: str = ""
    reconcileFlag: str = ""
    bankId: str = ""
    value: Decimal = Decimal(0)
    reconcileDate: str = ""
    id: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(
            payee=node.attrib["payee"],
            memo=node.attrib["memo"],
            shares=fraction_to_decimal(node.attrib["shares"]),
            number=node.attrib["number"],
            action=node.attrib["action"],
            price=fraction_to_decimal(node.attrib["price"]),
            account=node.attrib["account"],
            reconcileFlag=node.attrib["reconcileflag"],
            bankId=node.attrib["bankid"],
            value=fraction_to_decimal(node.attrib["value"]),
            reconcileDate=node.attrib["reconciledate"],
            id=node.attrib["id"],
        )
