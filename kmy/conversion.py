from decimal import Decimal
from fractions import Fraction


def fraction_to_decimal(value: str) -> Decimal:
    if not value:
        return Decimal(0)
    fraction = Fraction(value)
    return Decimal(fraction.numerator) / Decimal(fraction.denominator)
