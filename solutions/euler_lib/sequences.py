import math

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