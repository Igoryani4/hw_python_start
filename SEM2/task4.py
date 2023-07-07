import math
import decimal

decimal.getcontext().prec = 44

d = int(input('Ввыедите число'))

l = decimal.Decimal(math.pi * d)
print(l)

s = decimal.Decimal(math.pi * ((d ** 2) / 4))
print(s)
