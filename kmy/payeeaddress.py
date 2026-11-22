from dataclasses import dataclass

from .address import Address


@dataclass(frozen=True)
class PayeeAddress(Address):
    postCode: str = ""
    state: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(
            **cls._kwargs_from_xml(node),
            postCode=node.attrib["postcode"],
            state=node.attrib["state"],
        )
