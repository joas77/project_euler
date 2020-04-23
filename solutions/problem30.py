# https://projecteuler.net/problem=30

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from euler_lib.numbers import num_to_digitlist
    
if __name__ == "__main__":

    sums_fith_power = []

    for i in range(2, 1000000):
        if sum([d**5 for d in  num_to_digitlist(i)]) == i:
            sums_fith_power.append(i)

    print(f"solution = {sum(sums_fith_power)}")

