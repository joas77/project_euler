import itertools
from euler_lib import numbers


def is_pandigital_prod(a: int, b: int)->int:
    digits_a = numbers.num_to_digitlist(a)
    digits_b = numbers.num_to_digitlist(b)
    digits_c = numbers.num_to_digitlist(a * b)

    return len(digits_a) + len(digits_b) + len(digits_c) == 9 and\
        set(digits_a) | set(digits_b) | set(digits_c) == {1,2,3,4,5,6,7,8,9}


def solution():
    r = range(2, 10_000)
    products = set()
    for a, b in itertools.product(r, r):
        p = a * b
        if p not in products and is_pandigital_prod(a, b):
            print(f"pandigital product {a} x {b} = {p}")
            products.add(p)

    print(f"sum of products = {sum(products)}")

if __name__ == '__main__':
    solution()



