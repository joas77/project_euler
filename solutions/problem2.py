from euler_lib import sequences

N = int(4e6)
even_fibo_sum = 0
fibnums = sequences.fib_gen()
for i, f in enumerate(fibnums, 1):
    if f > N: break
    if f %2 == 0 and f <= int(N):
        even_fibo_sum += f

print(even_fibo_sum)

