from dataclasses import dataclass


@dataclass(frozen=True)
class CostCenter:
    @classmethod
    def from_xml(cls, node):
        return cls()
