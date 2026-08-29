import math
from euler_lib import numbers as nums

def factorial_chain(n:int):
    sums = set()
    s = n
    yield s
    while s not in sums:
        sums.add(s)
        s = sum(math.factorial(d) for d in nums.num_to_digitlist(s))
        yield s


def solution():
    LIMIT = 1_000_000
    non_repeating_terms = 60
    chains = 0
    for n in range(LIMIT):
        l = len(list(factorial_chain(n)))
        if l - 1 == non_repeating_terms:
            print(f"{n} factorial chain has {l-1} elements")
            chains += 1

    print("="*20)
    print(f"total chains with {non_repeating_terms} elements below {LIMIT}: {chains}")

if __name__ == '__main__':
    solution()
