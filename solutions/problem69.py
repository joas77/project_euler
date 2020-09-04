# https://projecteuler.net/problem=69

from math import gcd
 
def  phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)

if __name__ == "__main__":
    maximum = 0
    solution = 0
    for n in range(1, 1_000_001):
        r = n/phi(n)
        if r > maximum:
            maximum = r
            solution = n
        if n%10000 == 0:
            print(maximum, solution, r, n)

    print(f"solution: {solution}")