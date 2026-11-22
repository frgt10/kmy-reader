from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional

from .conversion import fraction_to_decimal
from .conversion import parse_date


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
    reconcileDate: Optional[date] = None
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
            reconcileDate=parse_date(node.attrib["reconciledate"]),
            id=node.attrib["id"],
        )
