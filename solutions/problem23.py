
# https://projecteuler.net/problem=23
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import itertools
import euler_lib.numbers as nums

if __name__ == "__main__":
    # first  find all abundant numbers until 28123
    abundants = []
    for i in range(1, 28_123 +1):
        if nums.is_abundant(i):
            abundants.append(i)

    print(f"there are {len(abundants)} abundant numbers from 1 to 28,123")

    numbers = set(range(1, 28_123 + 1))

    for x, y in itertools.combinations_with_replacement(abundants, 2):
        if x + y in numbers:
            numbers.remove(x+y)

    print(f"sum of integers which cannot be writen as the sum of two abundant numbers: {sum(numbers)}")