# https://projecteuler.net/problem=206

"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, (19 digits)
where each “_” is a single digit.
"""
    
import math
if __name__ == "__main__":
    n = 1

    max_number = 1929394959697989990
    max_sqrt = int(math.sqrt(max_number))
    n = max_sqrt

    while str(n*n)[::2] != "1234567890":
        if n%1000 == 0:
            print(n)
        n-=1

    print(f"{n}^2 = {n*n}")
