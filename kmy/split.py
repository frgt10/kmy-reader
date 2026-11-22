class Split:
    def __init__(
        self,
        payee: str = "",
        memo: str = "",
        shares: str = "",
        number: str = "",
        action: str = "",
        price: str = "",
        account: str = "",
        reconcileFlag: str = "",
        bankId: str = "",
        value: str = "",
        reconcileDate: str = "",
        id: str = "",
    ):
        self.payee = payee
        self.memo = memo
        self.shares = shares
        self.number = number
        self.action = action
        self.price = price
        self.account = account
        self.reconcileFlag = reconcileFlag
        self.bankId = bankId
        self.value = value
        self.reconcileDate = reconcileDate
        self.id = id

    def __repr__(self):
        return f"{self.__class__.__name__}(payee='{self.payee}', value='{self.value}')"

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
