# https://projecteuler.net/problem=21
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
from euler_lib.numbers import proper_divisors

def d(n):
    return sum(proper_divisors(n))

if __name__ == "__main__":
    amicable_pairs = []
    amicable_nums = set()
    for a in range(1, 10000+1):
        if a not in amicable_nums:
            b = d(a)
            if d(b) == a and a!=b:
                amicable_pairs.append((a,b))
                amicable_nums.update({a,b})

    print(amicable_pairs)
    print(f"sum of amicable numbers under 10000 = {sum(amicable_nums)}")
