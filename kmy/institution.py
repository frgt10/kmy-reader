from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from .institutionaddress import InstitutionAddress
from .pairs import pairs_dict_from_xml


@dataclass(frozen=True)
class Institution:
    id: str = ""
    sortCode: str = ""
    name: str = ""
    manager: str = ""
    address: InstitutionAddress = field(default_factory=InstitutionAddress)
    accountIds: List[str] = field(default_factory=list, compare=False)
    keyValuePairs: Dict[str, str] = field(default_factory=dict, compare=False)

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
