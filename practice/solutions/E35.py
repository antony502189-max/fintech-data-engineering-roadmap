def solve(data):
    from decimal import Decimal,ROUND_HALF_UP
    total=Decimal(data['scanned_gb'])*Decimal(data['price_gb'])+Decimal(data['hours'])*Decimal(data['price_hour'])
    return str(total.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))
