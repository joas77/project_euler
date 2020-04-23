# https://projecteuler.net/problem=40
"""
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

if __name__ == "__main__":
    champ_const = ""
    i = 0
    while len(champ_const) < 1000000:
        i+=1
        champ_const += str(i)


    result = 1
    for i in range(7):
        result *= int(champ_const[10**i - 1])
        print(champ_const[10**i - 1])

    print(f"solution: {result}")