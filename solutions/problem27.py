"""
Euler discovered the remarkable quadratic formula:
$n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 < n <= 39. 
However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when 
n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values $0 <= n <= 79$. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

$n^2 + an + b$, where $|a| < 1000$ and $|b| <= 1000
where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for 
consecutive values of n, starting with n = 0.
"""

from euler_lib.numbers import is_prime


def quadratics(a, b, n) -> int:
    return n*n + a*n + b

if __name__=="__main__":
    maxn = 0
    
    coeffs = 1,1
    trange = range(-1000, 1000 + 1)
    for a in trange:
        for b in trange:
            n = 0
            prime = True
            while prime:
                p = quadratics(a, b, n)
                prime = is_prime(p)
                if prime and n+1 > maxn:
                    maxn = n + 1
                    coeffs = a, b
                n += 1

    a,b = coeffs
    print(f"a={a}, b={b}")
    print(f"a*b = {a*b}")
