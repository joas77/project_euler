# https://projecteuler.net/problem=35

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

from euler_lib.numbers import num_to_digitlist, is_prime

def digits_rotations(n):
    digits = num_to_digitlist(n)
    num_digits = len(digits)
    rotations = [n]

    if num_digits == 1:
        yield rotations

    for _ in range(num_digits -1):
        
        d0 = digits[0]
        for  i in range(1, num_digits):
            digits[i-1] = digits[i]

        digits[-1] = d0
        n = int("".join(map(str, digits)))
        rotations.append(n)
        yield n

    # return rotations

if __name__ == "__main__":
    circular_primes = []

    for i in range(2,20):
        is_circular_prime = True
        for r in digits_rotations(i):
            if not is_prime(r):
                is_circular_prime = False
        
        if is_circular_prime:
            circular_primes.append(i)

    print(circular_primes)