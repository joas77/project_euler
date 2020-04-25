# https://projecteuler.net/problem=56

"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

if __name__ == "__main__":
    max_sum = 0
    for a in range(1,100):

        for b in range(1, 100):
            digits_sum = 0
            for d in str(a**b):
                digits_sum += int(d)

            max_sum = max(digits_sum, max_sum)

    print(f"solution: {max_sum}")