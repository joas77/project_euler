# https://projecteuler.net/problem=36

"""
The decimal number, 585 = 0b1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from euler_lib import numbers

if __name__ == "__main__":
    double_base_pals = []

    for i in range(1, 1_000_000):
        if numbers.is_palindrome(i):
            binstr = bin(i)[2:]
            if binstr == binstr[::-1]:
                double_base_pals.append(i)

    print(f"double base palindromes: {double_base_pals}")

    print(f"sum of double base palindromes: {sum(double_base_pals)}")

