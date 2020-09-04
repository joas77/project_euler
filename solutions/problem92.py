# https://projecteuler.net/problem=92

import euler_lib.numbers as euler

def square_digits(number:int)->int:
    chain = number
    if(chain==1 or chain==89):
        yield chain
    while not(chain==1 or chain==89):
        chain = sum([ d*d for d in euler.num_to_digitlist(chain)])
        #print(chain)
        yield chain

if __name__ == "__main__":
    
    count_89s = 0

    for i in range(1, int(10E6)):
        if i%1000==0:
            print(i)
        *_, last_chain = square_digits(i) # unpacking according to PEP 448
        if last_chain == 89:
            count_89s +=1
            #print(last_chain)

    print(f"solution: {count_89s}")
