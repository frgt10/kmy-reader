from typing import Optional

from .useraddress import UserAddress


class User(object):
    def __init__(
        self,
        email: str = "",
        name: str = "",
        address: Optional[UserAddress] = None,
    ):
        self.email = email
        self.name = name
        self.address = address if address is not None else UserAddress()

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

    @classmethod
    def from_xml(cls, node):
        return cls(
            email=node.attrib["email"],
            name=node.attrib["name"],
            address=UserAddress.from_xml(node.find("ADDRESS")),
        )
