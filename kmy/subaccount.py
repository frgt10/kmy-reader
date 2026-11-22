from dataclasses import dataclass


@dataclass(frozen=True)
class SubAccount:
    id: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(id=node.attrib["id"])
