from dataclasses import dataclass
from dataclasses import field
from typing import List

from .price import Price


@dataclass(frozen=True)
class Pricepair:
    curFrom: str = ""
    curTo: str = ""
    prices: List[Price] = field(default_factory=list, compare=False)

    @classmethod
    def from_xml(cls, node):
        prices = []
        for price_node in node:
            prices.append(Price.from_xml(price_node))
        return cls(
            curFrom=node.attrib["from"],
            curTo=node.attrib["to"],
            prices=prices,
        )
