import math
from euler_lib import sequences

digits = 1000
for i, f in enumerate(sequences.fib_gen(), 1):
    if int(math.log10(f)) + 1 == digits:
        print(i)
        break
