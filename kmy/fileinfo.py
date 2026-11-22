from dataclasses import dataclass
from datetime import date
from typing import Optional

from .conversion import parse_date


@dataclass(frozen=True)
class FileInfo:
    creationDate: Optional[date] = None
    lastModifiedDate: Optional[date] = None
    version: str = ""
    fixVersion: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(
            creationDate=parse_date(node.find("CREATION_DATE").attrib["date"]),
            lastModifiedDate=parse_date(node.find("LAST_MODIFIED_DATE").attrib["date"]),
            version=node.find("VERSION").attrib["id"],
            fixVersion=node.find("FIXVERSION").attrib["id"],
        )
