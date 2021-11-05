import math

def triangle(n: int) -> int:
    return int(n*(n+1)/2)

def pentagonal(n: int) -> int:
    return int(n*(3*n-1)/2)

def hexagonal(n: int) -> int:
    return int(n*(2*n - 1))

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