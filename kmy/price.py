from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional

from .conversion import fraction_to_decimal
from .conversion import parse_date


@dataclass(frozen=True)
class Price:
    date: Optional[date] = None
    source: str = ""
    price: Optional[Decimal] = None

    @classmethod
    def from_xml(cls, node):
        return cls(
            date=parse_date(node.attrib["date"]),
            source=node.attrib["source"],
            price=fraction_to_decimal(node.attrib["price"]),
        )
