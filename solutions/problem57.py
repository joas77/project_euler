# https://projecteuler.net/problem=57
from fractions import Fraction

iterations = 1000
frac = Fraction(numerator=1, denominator=2)
counter = 0

for it in range(iterations):
    sqrt2 = 1 + frac
    # print(sqrt2)
    digits_num = len(str(sqrt2.numerator))
    digits_den = len(str(sqrt2.denominator))

    if digits_num > digits_den:
        counter +=1

    frac = Fraction(numerator=1, denominator = 2 + frac)
    
print(f"There are {counter} fractions that contains a numerator with more digits than denominator in {iterations} expansions")