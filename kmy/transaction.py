from typing import List
from typing import Optional

from .split import Split


class Transaction:
    def __init__(
        self,
        postDate: str = "",
        memo: str = "",
        commodity: str = "",
        entryDate: str = "",
        id: str = "",
        splits: Optional[List[Split]] = None,
    ):
        self.postDate = postDate
        self.memo = memo
        self.commodity = commodity
        self.entryDate = entryDate
        self.id = id
        self.splits = splits if splits is not None else []

    def __repr__(self):
        return f"{self.__class__.__name__}(postDate='{self.postDate}', memo='{self.memo}')"

    @classmethod
    def from_xml(cls, node):
        splits = []
        split_nodes = node.find("SPLITS")
        if split_nodes is not None:
            for split_node in split_nodes:
                splits.append(Split.from_xml(split_node))
        return cls(
            postDate=node.attrib["postdate"],
            memo=node.attrib["memo"],
            commodity=node.attrib["commodity"],
            entryDate=node.attrib["entrydate"],
            id=node.attrib["id"],
            splits=splits,
        )
