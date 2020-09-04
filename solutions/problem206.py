# https://projecteuler.net/problem=206

"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, (19 digits)
where each “_” is a single digit.
"""


def is_concealed_square(n):
    n_squared_str = str(n*n)

    for i, digit in enumerate(n_squared_str[0::2], start=1):
        if int(digit)%10 != i: # Falta comparar con el 0!!
            return False

    return True        

if __name__ == "__main__":
    n = int(1e9)

    while not is_concealed_square(n):
        if n%10000 == 0:
            print(n)
        n += 1

    print(f"{n}^2 = {n*n}")
