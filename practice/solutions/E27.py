def solve(data):
    from decimal import Decimal,ROUND_HALF_EVEN
    from fintech_lab.money import EXPONENTS
    major=Decimal(data['minor'])/(10**EXPONENTS[data['from']])
    scaled=major*Decimal(data['rate'])*(10**EXPONENTS[data['to']])
    return int(scaled.to_integral_value(rounding=ROUND_HALF_EVEN))
