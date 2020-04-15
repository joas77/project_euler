# https://projecteuler.net/problem=52
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

if __name__ == "__main__":
    n = 1
    found = False
    solution = -1
    while not found:
        digits2set = lambda n: {int(c) for c in str(n)}
        n_digits = digits2set(n)

        found = True
        for x in range(2, 6+1):
            x_digits = digits2set(x*n)
            solution = n
            if len(n_digits.symmetric_difference(x_digits)) !=0:
                found = False
                break
        n+=1

    print(f"solution: {solution}")
