# It was proposed by Christian Goldbach that every odd composite number can be written
# as the sum of a prime and twice a square.

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written
# as the sum of a prime and twice a square?
# n = p + 2k^2
# (n - p)/2 = k^2

import math
from euler_lib import numbers

primegen = numbers.primes()
primes = set()
p = next(primegen)
primes.add(p)
conjecture = True

for pnext in primegen:
    primes.add(p)
    for composite in range(p + 1, pnext):
        if composite % 2 != 0:
            for prime in primes:
                conjecture = False
                if (composite - prime) %2 == 0:
                    # search the square
                    square = (composite - prime) // 2
                    sqrt = int(math.sqrt(square))
                    if sqrt * sqrt == square:
                        print(f"{composite} = {prime} + 2 * {sqrt}^2")
                        conjecture = True
                        break
            print(composite)
            if not conjecture:
                print(f"conjecture is false composite that not fullfills it is: {composite}")
                exit()
    p = pnext
