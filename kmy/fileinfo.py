class FileInfo:
    def __init__(
        self,
        creationDate: str = "",
        lastModifiedDate: str = "",
        version: str = "",
        fixVersion: str = "",
    ):
        self.creationDate = creationDate
        self.lastModifiedDate = lastModifiedDate
        self.version = version
        self.fixVersion = fixVersion

    def __repr__(self):
        return f"{self.__class__.__name__}(creationDate='{self.creationDate}', lastModifiedDate={self.lastModifiedDate})"

    @classmethod
    def from_xml(cls, node):
        return cls(
            creationDate=node.find("CREATION_DATE").attrib["date"],
            lastModifiedDate=node.find("LAST_MODIFIED_DATE").attrib["date"],
            version=node.find("VERSION").attrib["id"],
            fixVersion=node.find("FIXVERSION").attrib["id"],
        )
