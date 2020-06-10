from decimal import Decimal
from fractions import Fraction

a = filter(lambda _ : _, [None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), [], {}, (), '', b'', set(), range(0)])
print(True or list(a))print(False or list(a))