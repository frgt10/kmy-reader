class Tag:
    def __init__(
        self,
        closed: bool = False,
        tagColor: str = "",
        name: str = "",
        id: str = "",
    ):
        self.closed = closed
        self.tagColor = tagColor
        self.name = name
        self.id = id

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

    @classmethod
    def from_xml(cls, node):
        return cls(
            closed=(node.attrib["closed"] != "0"),
            tagColor=node.attrib["tagcolor"],
            name=node.attrib["name"],
            id=node.attrib["id"],
        )
