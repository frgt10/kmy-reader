from datetime import date
from datetime import datetime
from decimal import Decimal
from fractions import Fraction
from typing import Optional


def fraction_to_decimal(value: str) -> Decimal:
    if not value:
        return Decimal(0)
    fraction = Fraction(value)
    return Decimal(fraction.numerator) / Decimal(fraction.denominator)


def parse_date(value: str) -> Optional[date]:
    value = value.strip()
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
