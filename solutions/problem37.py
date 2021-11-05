#https://projecteuler.net/problem=37
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from euler_lib.numbers import is_prime, primes, truncate_left, truncate_right


if __name__=="__main__":
    truncatable_primes = []
    p = primes()
    while len(truncatable_primes) < 11:
        next_prime = next(p)
        
        if next_prime <= 7:
            continue

        is_truncatable = True
        l = truncate_left(next_prime)
        r = truncate_right(next_prime)
        next(l)
        next(r)
        for left, right in zip(l, r):
            if not is_prime(left) or not is_prime(right):
                is_truncatable = False
                break
        
        if is_truncatable:
            truncatable_primes.append(next_prime)
            print(next_prime)
        

    print(f"result = {sum(truncatable_primes)}")