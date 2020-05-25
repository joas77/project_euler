# problem 28: https://projecteuler.net/problem=28
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

S = {1, 3, 5, 7, 9, 13, 17, 21, 25}

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Analysis:
L[k] = 2 * ceil(k/4) + 1
S[k] =  s[k-1] + L[k] - 1
S[k] =  s[k-1] + 2 * ceil(k/4)
s[0] = 1
"""
# import math

# def spiral_seq(n):
#     s = 1
#     for k in range(n):
#         s = s + 2 * math.ceil(k/4)
#         yield s

from euler_lib.sequences import spiral_seq

print(f"sum of the numbers on the diagonasl in a 1001 x 1001 spiral: {sum(spiral_seq(2001))}")