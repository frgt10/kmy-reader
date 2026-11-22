class Address:
    def __init__(
        self,
        city: str = "",
        street: str = "",
        telephone: str = "",
    ):
        self.city = city
        self.street = street
        self.telephone = telephone

    @staticmethod
    def _kwargs_from_xml(node):
        return {
            "city": node.attrib["city"],
            "street": node.attrib["street"],
            "telephone": node.attrib["telephone"],
        }

    @classmethod
    def from_xml(cls, node):
        return cls(**cls._kwargs_from_xml(node))
