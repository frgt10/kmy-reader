from .address import Address


class PayeeAddress(Address):
    def __init__(
        self,
        city: str = "",
        street: str = "",
        telephone: str = "",
        postCode: str = "",
        state: str = "",
    ):
        super().__init__(city=city, street=street, telephone=telephone)
        self.postCode = postCode
        self.state = state

    @classmethod
    def from_xml(cls, node):
        return cls(
            **cls._kwargs_from_xml(node),
            postCode=node.attrib["postcode"],
            state=node.attrib["state"],
        )
