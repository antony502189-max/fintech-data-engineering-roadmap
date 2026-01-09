"""Currency-aware exact money parsing: never accept binary floating point."""
from decimal import Decimal, InvalidOperation, localcontext

EXPONENTS = {"USD": 2, "EUR": 2, "JPY": 0, "KWD": 3}

def to_minor(amount: str, currency: str) -> int:
    if not isinstance(amount, str):
        raise TypeError("Money must enter as a decimal string")
    if len(amount) > 128:
        raise ValueError("Amount string exceeds teaching contract limit")
    if currency not in EXPONENTS:
        raise ValueError("Unsupported currency")
    try:
        value = Decimal(amount)
    except InvalidOperation as exc:
        raise ValueError("Invalid amount") from exc
    if not value.is_finite():
        raise ValueError("Non-finite amount")
    if value.is_zero():
        return 0
    magnitude = value.copy_abs()
    if magnitude < Decimal(1) / (10 ** EXPONENTS[currency]):
        raise ValueError("Amount has too many fractional digits")
    # Default Decimal precision could silently round a long near-cent value.
    with localcontext() as context:
        context.prec = max(28, len(value.as_tuple().digits) + EXPONENTS[currency] + 1)
        if magnitude > Decimal(9_000_000_000_000_000) / (10 ** EXPONENTS[currency]):
            raise ValueError("Amount exceeds teaching contract limit")
        scaled = value * (10 ** EXPONENTS[currency])
        if scaled != scaled.to_integral_value():
            raise ValueError("Amount has too many fractional digits")
        minor = int(scaled)
    return minor
