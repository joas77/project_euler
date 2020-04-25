# https://projecteuler.net/problem=36

"""
The decimal number, 585 = 0b1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

if __name__ == "__main__":
    double_base_pals = [1,3,5,7,9]

    for i in range(1, 100):
       pal_str = str(i) + str(i)[::-1]
       pal = int(pal_str)
       binary = bin(pal)[2::]

       if binary == binary[::-1]:
           double_base_pals.append(pal)

    print(f"double base palindromes: {double_base_pals}")

    print(f"sum of double base palindromes: {sum(double_base_pals)}")


    # TODO: check solution in https://www.geeksforgeeks.org/double-base-palindrome/
    # and fix script
