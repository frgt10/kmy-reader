from typing import Dict
from typing import List
from typing import Optional

from .payeeaddress import PayeeAddress


class Payee:
    def __init__(
        self,
        reference: str = "",
        name: str = "",
        email: str = "",
        id: str = "",
        matchingEnabled: bool = False,
        address: Optional[PayeeAddress] = None,
        payeeIdentifiers: Optional[List[Dict[str, str]]] = None,
        usingMatchkey: bool = False,
        matchkeys: Optional[List[str]] = None,
    ):
        self.reference = reference
        self.name = name
        self.email = email
        self.id = id
        self.matchingEnabled = matchingEnabled
        self.address = address if address is not None else PayeeAddress()
        self.payeeIdentifiers = payeeIdentifiers if payeeIdentifiers is not None else []
        self.usingMatchkey = usingMatchkey
        self.matchkeys = matchkeys if matchkeys is not None else []

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

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
