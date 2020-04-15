# https://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
import sys
sys.setrecursionlimit(10**6)
def collatz_seq(n):
    if n==1:
        yield n
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        yield n

def my_brute_force_solution():
    N = 1000000 
    used_nums = set()
    seq_lens = dict()
    while N > 1:
        if N not in used_nums:
            seq = list(collatz_seq(N))
            seq_lens[N] = seq
            used_nums.union(seq)
        N-=1

    longest_seq = max(seq_lens.items(), key=lambda x: len(x[1]))
    print(f"Number which yields longest collatz sequence under 1000000: {longest_seq[0]}") 

def count_chain(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + count_chain(n/2)
    else:
        return 1 + count_chain(3*n +1)


def brute_force():
    longest_chain = 0
    answer = 1

    for number in range(int(1e6)):
        if count_chain(number) > longest_chain:
            longest_chain = count_chain(number)
            answer = number

    print(answer)

if __name__ == "__main__":
    #brute_force()
    #print(count_chain(13))
    my_brute_force_solution()
