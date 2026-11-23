from dataclasses import dataclass
from decimal import Decimal

from .conversion import fraction_to_decimal
from .pairs import pairs_dict_from_xml


@dataclass(frozen=True)
class Security:
    id: str = ""
    symbol: str = ""
    name: str = ""
    saf: int = 1
    pp: int = 2
    tradingCurrency: str = ""
    tradingMarket: str = ""
    type: str = ""
    roundingMethod: str = ""
    onlineFactor: Decimal = Decimal(1)
    onlineSource: str = ""
    securityId: str = ""

    @classmethod
    def from_xml(cls, node):
        pairs = pairs_dict_from_xml(node.find("KEYVALUEPAIRS"))
        online_factor = Decimal(1)
        if "kmm-online-factor" in pairs:
            online_factor = fraction_to_decimal(pairs["kmm-online-factor"])
        return cls(
            id=node.attrib["id"],
            symbol=node.attrib["symbol"],
            name=node.attrib["name"],
            saf=int(node.attrib["saf"]),
            pp=int(node.attrib["pp"]),
            tradingCurrency=node.attrib["trading-currency"],
            tradingMarket=node.attrib.get("trading-market", ""),
            type=node.attrib["type"],
            roundingMethod=node.attrib["rounding-method"],
            onlineFactor=online_factor,
            onlineSource=pairs.get("kmm-online-source", ""),
            securityId=pairs.get("kmm-security-id", ""),
        )
