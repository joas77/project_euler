"""
https://projecteuler.net/problem=26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import re

def reciprocal(d):
    """
    returns a string with 'exact' decimal representation of 1/d
    infinite sequences are represented in this way (abcd)
    example:
    1/3 = 0.(3) = 0.333...
    1/7 = 0.1(428751) = 0.124871248571...
    """
    i = 0
    if d == 1:
        return "1.0"

    decimals = []
    remainders = dict() # dict to save remainder: position
    is_recurring = False
    rest = 1
    while not is_recurring and rest != 0:
        decimals.append(str(10*rest//d))
        rest = (10*rest)%d
        if rest in remainders:
            is_recurring = True
            position = remainders[rest] + 1
            r = decimals[position]
            decimals[position] = f"({r}"
            decimals[-1] = f"{decimals[-1]})"
        else:
            remainders[rest] = i
        
        i += 1


    return "0."+"".join(decimals)


if __name__ == "__main__":
    seq_reg = re.compile(r"\(\d+\)")
    longest_rec = ""
    max_len = 0
    d = 0
    for i in range(1, 1000 + 1):
        rec = reciprocal(i)
        matches = seq_reg.findall(rec)
        if matches:
            print(rec)
            cycle = matches[0]
            cycle_len = len(cycle) - 2
            if cycle_len >= max_len:
                longest_rec = rec
                max_len = cycle_len
                d = i


    print("longest recurring cycle:")
    print(f"1/{d} = {longest_rec}")
                

