from dataclasses import dataclass
from dataclasses import field
from datetime import date
from typing import Dict
from typing import List
from typing import Optional

from .conversion import parse_date
from .pairs import pairs_dict_from_xml
from .subaccount import SubAccount


@dataclass(frozen=True)
class Account:
    number: str = ""
    lastModified: Optional[date] = None
    institution: str = ""
    name: str = ""
    currency: str = ""
    parentAccount: str = ""
    lastReconciled: Optional[date] = None
    description: str = ""
    type: str = ""
    opened: Optional[date] = None
    id: str = ""
    subAccounts: List[SubAccount] = field(default_factory=list, compare=False)
    keyValuePairs: Dict[str, str] = field(default_factory=dict, compare=False)

    @classmethod
    def from_xml(cls, node):
        subaccounts = []
        subaccount_nodes = node.find("SUBACCOUNTS")
        if subaccount_nodes is not None:
            for subaccount_node in subaccount_nodes:
                subaccounts.append(SubAccount.from_xml(subaccount_node))
        return cls(
            number=node.attrib["number"],
            lastModified=parse_date(node.attrib["lastmodified"]),
            institution=node.attrib["institution"],
            name=node.attrib["name"],
            currency=node.attrib["currency"],
            parentAccount=node.attrib["parentaccount"],
            lastReconciled=parse_date(node.attrib["lastreconciled"]),
            description=node.attrib["description"],
            type=node.attrib["type"],
            opened=parse_date(node.attrib["opened"]),
            id=node.attrib["id"],
            subAccounts=subaccounts,
            keyValuePairs=pairs_dict_from_xml(node.find("KEYVALUEPAIRS")),
        )
