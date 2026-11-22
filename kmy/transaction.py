from dataclasses import dataclass
from dataclasses import field
from datetime import date
from typing import List
from typing import Optional

from .conversion import parse_date
from .split import Split


@dataclass(frozen=True)
class Transaction:
    postDate: Optional[date] = None
    memo: str = ""
    commodity: str = ""
    entryDate: Optional[date] = None
    id: str = ""
    splits: List[Split] = field(default_factory=list, compare=False)

    @classmethod
    def from_xml(cls, node):
        splits = []
        split_nodes = node.find("SPLITS")
        if split_nodes is not None:
            for split_node in split_nodes:
                splits.append(Split.from_xml(split_node))
        return cls(
            postDate=parse_date(node.attrib["postdate"]),
            memo=node.attrib["memo"],
            commodity=node.attrib["commodity"],
            entryDate=parse_date(node.attrib["entrydate"]),
            id=node.attrib["id"],
            splits=splits,
        )
