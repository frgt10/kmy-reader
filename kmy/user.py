from dataclasses import dataclass
from dataclasses import field

from .useraddress import UserAddress


@dataclass(frozen=True)
class User:
    email: str = ""
    name: str = ""
    address: UserAddress = field(default_factory=UserAddress)

    @classmethod
    def from_xml(cls, node):
        return cls(
            email=node.attrib["email"],
            name=node.attrib["name"],
            address=UserAddress.from_xml(node.find("ADDRESS")),
        )
