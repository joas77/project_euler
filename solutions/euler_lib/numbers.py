import math

def divisors(n:int)->set:
    divs = set()
    for i in range(1, n//4 + 1):
        if n%i == 0:
            divs.add(i)
            divs.add(n//i)
    divs.add(n)
    return divs

def proper_divisors(n:int)->set:
    pdivisors = divisors(n)
    pdivisors.discard(n)
    return pdivisors

def is_prime(n:int)->bool:
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def primes():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1

def primes_below(n:int):
    for i in range(2, n+1):
        if is_prime(i):
            yield i

def num_to_digitlist(n:int)->list:
    return [int(d) for d in str(n)]

def truncate_right(n):
    digits = num_to_digitlist(n)
    while digits:
        s = "".join(str(d) for d in digits)
        yield int(s)
        digits.pop()

def truncate_left(n):
    digits = num_to_digitlist(n)
    while digits:
        s = "".join(str(d) for d in digits)
        yield int(s)
        digits.pop(0)

def is_palindrome(n:int)->bool:
    return str(n) == str(n)[::-1]

def is_square(n:int)->bool:
    sqrt = int(math.sqrt(n))
    return sqrt*sqrt == n