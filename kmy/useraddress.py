from .address import Address


class UserAddress(Address):
    def __init__(
        self,
        city: str = "",
        street: str = "",
        telephone: str = "",
        zipcode: str = "",
        county: str = "",
    ):
        super().__init__(city=city, street=street, telephone=telephone)
        self.zipcode = zipcode
        self.county = county

    @classmethod
    def from_xml(cls, node):
        return cls(
            **cls._kwargs_from_xml(node),
            zipcode=node.attrib["zipcode"],
            county=node.attrib["county"],
        )
