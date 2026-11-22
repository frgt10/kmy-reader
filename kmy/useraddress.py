from dataclasses import dataclass

from .address import Address


@dataclass(frozen=True)
class UserAddress(Address):
    zipcode: str = ""
    county: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(
            **cls._kwargs_from_xml(node),
            zipcode=node.attrib["zipcode"],
            county=node.attrib["county"],
        )
