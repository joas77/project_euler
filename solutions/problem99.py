# https://projecteuler.net/problem=99
"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more difficult, 
as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with 
a base/exponent pair on each line, determine which line number has the greatest numerical value.
NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import math
if __name__=="__main__":
    nums_base_exp = []
    with open("./files/p099_base_exp.txt") as base_exp:
        for line in base_exp.readlines():
            b, e = line.split(",")
            nums_base_exp.append((int(b), int(e)))

    nums_sorted = sorted(nums_base_exp, key=lambda num: num[1]*math.log(num[0]))

    index = nums_base_exp.index(nums_sorted[-1])

    print(index + 1)