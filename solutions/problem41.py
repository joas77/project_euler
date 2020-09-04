# https://projecteuler.net/problem=41
import itertools
import euler_lib.numbers

def is_pandigital(number:int, n:int)->bool:
    """
    :param number: number to test 
    :param n: number of digits
    :returns: bool- True if number is n-digits pandigital
    """
    if len(str(number)) != n:
        return False

    digits = euler_lib.numbers.num_to_digitlist(number)
    for digit in range(1, n+1):
        if digits.count(digit) != 1:
            return False

    return True

if __name__ == "__main__":
    n = 987654321 # largest 9-digit pandigital
    number_digits = len(str(n))

    # testing is_pandigital function before to enter the loop
    assert is_pandigital(n,9)
    assert is_pandigital(1234, 4)
    assert not is_pandigital(4353, 4)

    found_pandigital = False
    i=9
    
    while not found_pandigital:

        pandigitals = [int("".join(map(str, p))) for p in itertools.permutations(range(1, i+1))]
        pandigitals.reverse()

        for p in pandigitals:
            if euler_lib.numbers.is_prime(p):
                print(f"solution found: {p} !!")
                found_pandigital = True
                break
        i -= 1
