# https://projecteuler.net/problem=92

import euler_lib.sequences as seq


if __name__ == "__main__":
    
    count_89s = 0

    for i in range(1, int(10E6)):
        if i%10_000==0:
            print(f"**** ith {i} ****")
            print(f"{count_89s} has been found that end in 89")

        for node in seq.square_digit_chain(i):
            if node == 89:
                count_89s +=1
                # print(i)
 
    count_89s+=1
    print(f"solution: {count_89s}")
