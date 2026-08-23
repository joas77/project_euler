import math


def solution():
    N = 100
    solutions = 0
    for n in range(1, N+1):
        for r in range(1, N+1):
            if math.comb(n, r) > 1e6:
                print(f"C({n}, {r}) > 1M")
                solutions += 1

    print(f"C(n, r) > 1M, 1 <= n <= 100  has {solutions} solutions")

if __name__ == '__main__':
    solution()
