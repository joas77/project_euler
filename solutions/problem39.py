import itertools
import math
import collections

def solution():

    r = range(1, 1000)
    solutions = collections.defaultdict(int)
    for a, b in itertools.product(r, r):
        c = math.hypot(a, b)
        p = a + b + c
        if c.is_integer() and p <= 1000:
            print(f"Found triangle, {a}, {b}, {c}")
            solutions[p]+=1

    print(sorted(solutions.items(), key=lambda item: item[1]))

if __name__ == '__main__':
    solution()
