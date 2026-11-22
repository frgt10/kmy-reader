from dataclasses import dataclass


@dataclass(frozen=True)
class FileInfo:
    creationDate: str = ""
    lastModifiedDate: str = ""
    version: str = ""
    fixVersion: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(
            creationDate=node.find("CREATION_DATE").attrib["date"],
            lastModifiedDate=node.find("LAST_MODIFIED_DATE").attrib["date"],
            version=node.find("VERSION").attrib["id"],
            fixVersion=node.find("FIXVERSION").attrib["id"],
        )
