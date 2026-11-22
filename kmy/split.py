from dataclasses import dataclass


@dataclass(frozen=True)
class Split:
    payee: str = ""
    memo: str = ""
    shares: str = ""
    number: str = ""
    action: str = ""
    price: str = ""
    account: str = ""
    reconcileFlag: str = ""
    bankId: str = ""
    value: str = ""
    reconcileDate: str = ""
    id: str = ""

    @classmethod
    def from_xml(cls, node):
        return cls(
            payee=node.attrib["payee"],
            memo=node.attrib["memo"],
            shares=node.attrib["shares"],
            number=node.attrib["number"],
            action=node.attrib["action"],
            price=node.attrib["price"],
            account=node.attrib["account"],
            reconcileFlag=node.attrib["reconcileflag"],
            bankId=node.attrib["bankid"],
            value=node.attrib["value"],
            reconcileDate=node.attrib["reconciledate"],
            id=node.attrib["id"],
        )
