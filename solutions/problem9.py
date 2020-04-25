# https://projecteuler.net/problem=9

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

def solution():
    solution = 0
    for a in range(1,500):
        for b in range(1, 500):
            c = int(math.sqrt(a*a + b*b))
            if a+b+c == 1000 and a*a + b*b == c*c:
                solution = a*b*c
                print(a,b,c)
                return solution

    return None

if __name__ == "__main__":
    
    print(f"solution: {solution()} ")
            