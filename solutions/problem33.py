# https://projecteuler.net/problem=33

import functools
import fractions
from euler_lib.numbers import num_to_digitlist

if __name__ == "__main__":
    
    for x in range(10, 99):
        for y in range(x+1, 100):
            # print(f"{x}/{y}")
            nums_num = num_to_digitlist(x)
            nums_den = num_to_digitlist(y)
            num = functools.reduce(lambda x, y: x*y, nums_num)
            den = functools.reduce(lambda x, y: x*y, nums_den)
            if den != 0 and fractions.Fraction(num, den) == fractions.Fraction(x,y):
                print(f"{x}/{y}")

    """
    Solution is a mix between code and manual calculations:
    previous code snips returns:
    
    14/63 
    15/24
    16/64
    18/45
    19/95
    26/65
    49/98

    from previous output we are only interested in:
    16/64 = 1/4
    19/95 = 1/5
    26/65 = 2/5
    49/98 = 4/8 = 1/2

    1/4 * 1/5 * 2*/5 * 1/2 = 2/(4*5*5*2) = 1/100

    """