from dataclasses import dataclass


@dataclass(frozen=True)
class Tag:
    closed: bool = False
    tagColor: str = ""
    name: str = ""
    id: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(
            closed=(node.attrib["closed"] != "0"),
            tagColor=node.attrib["tagcolor"],
            name=node.attrib["name"],
            id=node.attrib["id"],
        )
