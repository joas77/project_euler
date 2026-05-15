# https://projecteuler.net/problem=7

from euler_lib import numbers

N =  10_001

for p in numbers.primegen(N): pass

print(f"{N}th prime: {p}")
