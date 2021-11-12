# https://projecteuler.net/problem=47
"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""
import euler_lib.numbers as nums

if __name__ == "__main__": 
    integers_factors = []
    prime_factors_count = 4
    i = 2
    while len(integers_factors) < 4:
        if len(nums.distinct_prime_factors(i)) - 1 ==prime_factors_count:
            if len(integers_factors) > 0:
                number = integers_factors[-1]
                if number + 1 != i:
                    integers_factors = []
                integers_factors.append(i)
            else:
                integers_factors.append(i)
        i+=1

    print(integers_factors)