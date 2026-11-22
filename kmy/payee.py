from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from .payeeaddress import PayeeAddress


@dataclass(frozen=True)
class Payee:
    reference: str = ""
    name: str = ""
    email: str = ""
    id: str = ""
    matchingEnabled: bool = False
    address: PayeeAddress = field(default_factory=PayeeAddress)
    payeeIdentifiers: List[Dict[str, str]] = field(default_factory=list, compare=False)
    usingMatchkey: bool = False
    matchkeys: List[str] = field(default_factory=list, compare=False)

    @classmethod
    def from_xml(cls, node):
        address_node = node.find("ADDRESS")
        address = (
            PayeeAddress.from_xml(address_node)
            if address_node is not None
            else PayeeAddress()
        )
        matchkey = node.attrib.get("matchkey", "")
        return cls(
            reference=node.attrib["reference"],
            name=node.attrib["name"],
            email=node.attrib["email"],
            id=node.attrib["id"],
            matchingEnabled=(node.attrib["matchingenabled"] != "0"),
            address=address,
            payeeIdentifiers=[
                payee_identifier_node.attrib.copy()
                for payee_identifier_node in node.findall("payeeIdentifier")
            ],
            usingMatchkey=node.attrib.get("usingmatchkey", "0") != "0",
            matchkeys=matchkey.split("\n") if matchkey else [],
        )

    def matched_by(self, **kwargs: Dict[str, str]) -> bool:
        def is_match(candidate: Dict[str, str]) -> bool:
            for key, val in kwargs.items():
                if candidate.get(key, None) != val:
                    return False
            return True

        for identifier in self.payeeIdentifiers:
            if is_match(identifier):
                return True

        return False
