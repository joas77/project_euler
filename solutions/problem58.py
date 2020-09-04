# https://projecteuler.net/problem=58

import math
from euler_lib.sequences import inf_spiral_seq
from euler_lib.numbers import is_prime

if __name__ == "__main__":
    prime_ratio = 1
    spiral = inf_spiral_seq()
    i=1
    L = 0
    prime_counter = 0
    while prime_ratio >= 0.1 or prime_ratio == 0:
        s = next(spiral)
        if is_prime(s):
            prime_counter += 1
        prime_ratio = prime_counter/i
        i+=1
        L = 2 * math.ceil(i/4) + 1 # see problem 28 solution

    print(s, prime_ratio, L)
    # L[k] = 2 * ceil(k/4) + 1

    #for k, s in enumerate(spiral_seq(50), start=1):
        # print(2*math.ceil(k/4)+1,s)
