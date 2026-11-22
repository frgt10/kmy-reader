from dataclasses import dataclass

from .address import Address


@dataclass(frozen=True)
class InstitutionAddress(Address):
    zip: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(**cls._kwargs_from_xml(node), zip=node.attrib["zip"])
