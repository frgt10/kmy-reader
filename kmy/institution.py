from typing import Dict
from typing import List
from typing import Optional

from .institutionaddress import InstitutionAddress
from .pairs import pairs_dict_from_xml


class Institution:
    def __init__(
        self,
        id: str = "",
        sortCode: str = "",
        name: str = "",
        manager: str = "",
        address: Optional[InstitutionAddress] = None,
        accountIds: Optional[List[str]] = None,
        keyValuePairs: Optional[Dict[str, str]] = None,
    ):
        self.id = id
        self.sortCode = sortCode
        self.name = name
        self.manager = manager
        self.address = address if address is not None else InstitutionAddress()
        self.accountIds = accountIds if accountIds is not None else []
        self.keyValuePairs = keyValuePairs if keyValuePairs is not None else {}

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

    @classmethod
    def from_xml(cls, node):
        address_node = node.find("ADDRESS")
        address = (
            InstitutionAddress.from_xml(address_node)
            if address_node is not None
            else InstitutionAddress()
        )
        account_ids = []
        for account_id_node in node.find("ACCOUNTIDS"):
            account_ids.append(account_id_node.attrib["id"])
        return cls(
            id=node.attrib["id"],
            sortCode=node.attrib["sortcode"],
            name=node.attrib["name"],
            manager=node.attrib["manager"],
            address=address,
            accountIds=account_ids,
            keyValuePairs=pairs_dict_from_xml(node.find("KEYVALUEPAIRS")),
        )
