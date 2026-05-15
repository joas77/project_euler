import math
from functools import cache

from . import numbers

@cache
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

@cache
def fib_gen(n):
    if n == 0: return 0
    if n == 1: return 1
    yield fib(n-1) + fib(n-2)


def triangle(n: int) -> int:
    return int(n*(n+1)/2)

def square(n: int) -> int:
    return n*(n+1)*(2*n+1)/6

def pentagonal(n: int) -> int:
    return int(n*(3*n-1)/2)

def hexagonal(n: int) -> int:
    return int(n*(2*n - 1))

def square_digit_chain(n):
    digits = numbers.num_to_digitlist(n)
    node = n

    while 1 != node != 89:
        node = sum(d*d for d in digits)
        digits = numbers.num_to_digitlist(node)
        yield node


def spiral_seq(n):
    s = 1
    for k in range(n):
        s = s + 2 * math.ceil(k/4)
        yield s

def inf_spiral_seq():
    s=1
    k = 0
    while True:
        s = s + 2*math.ceil(k/4)
        k += 1
        yield s
