class SubAccount:
    def __init__(self, id: str = ""):
        self.id = id

    def __repr__(self):
        return f"{self.__class__.__name__}(id='{self.id}')"

    @classmethod
    def from_xml(cls, node):
        return cls(id=node.attrib["id"])
