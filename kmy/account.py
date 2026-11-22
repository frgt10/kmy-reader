from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from .pairs import pairs_dict_from_xml
from .subaccount import SubAccount


@dataclass(frozen=True)
class Account:
    number: str = ""
    lastModified: str = ""
    institution: str = ""
    name: str = ""
    currency: str = ""
    parentAccount: str = ""
    lastReconciled: str = ""
    description: str = ""
    type: str = ""
    opened: str = ""
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
            lastModified=node.attrib["lastmodified"],
            institution=node.attrib["institution"],
            name=node.attrib["name"],
            currency=node.attrib["currency"],
            parentAccount=node.attrib["parentaccount"],
            lastReconciled=node.attrib["lastreconciled"],
            description=node.attrib["description"],
            type=node.attrib["type"],
            opened=node.attrib["opened"],
            id=node.attrib["id"],
            subAccounts=subaccounts,
            keyValuePairs=pairs_dict_from_xml(node.find("KEYVALUEPAIRS")),
        )
