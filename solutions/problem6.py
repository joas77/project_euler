from euler_lib import sequences

N = 100

sum_sqr_diff = sequences.triangle(N)**2 - sequences.square(N)
print(sum_sqr_diff)
