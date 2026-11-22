from .address import Address


class InstitutionAddress(Address):
    def __init__(
        self,
        city: str = "",
        street: str = "",
        telephone: str = "",
        zip: str = "",
    ):
        super().__init__(city=city, street=street, telephone=telephone)
        self.zip = zip

    @classmethod
    def from_xml(cls, node):
        return cls(**cls._kwargs_from_xml(node), zip=node.attrib["zip"])
