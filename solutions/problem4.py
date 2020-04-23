# https://projecteuler.net/problem=4

"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

from euler_lib.numbers import  proper_divisors, is_palindrome

if __name__ == "__main__":
    found = False
    num = 999
    largest_pal = 0
    pal1, pal2 = 0,0
    while not found:
        pal = int(str(num) + str(num)[::-1])
        for div in proper_divisors(pal):

            if len(str(div)) == 3  and len(str(pal//div)) == 3:
                found = True
                largest_pal = pal
                pal1 = div
                pal2 = pal//div
        
        num -= 1

    print(f"largest pal = {largest_pal} = {pal1}*{pal2}")

