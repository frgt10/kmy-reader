from typing import Dict
from typing import List
from typing import Optional

from .pairs import pairs_dict_from_xml
from .subaccount import SubAccount


class Account:
    def __init__(
        self,
        number: str = "",
        lastModified: str = "",
        institution: str = "",
        name: str = "",
        currency: str = "",
        parentAccount: str = "",
        lastReconciled: str = "",
        description: str = "",
        type: str = "",
        opened: str = "",
        id: str = "",
        subAccounts: Optional[List[SubAccount]] = None,
        keyValuePairs: Optional[Dict[str, str]] = None,
    ):
        self.number = number
        self.lastModified = lastModified
        self.institution = institution
        self.name = name
        self.currency = currency
        self.parentAccount = parentAccount
        self.lastReconciled = lastReconciled
        self.description = description
        self.type = type
        self.opened = opened
        self.id = id
        self.subAccounts = subAccounts if subAccounts is not None else []
        self.keyValuePairs = keyValuePairs if keyValuePairs is not None else {}

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', currency={self.currency})"

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
