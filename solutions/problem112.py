from euler_lib import numbers as nums
def is_sorted(l):
    ls = sorted(l)
    return l == ls or l == ls[::-1]

def solution():
    bouncy_counter = 0
    bouncy_prop = 0
    n = 100
    while bouncy_prop < 99:
        if nums.is_bouncy(n):
            bouncy_counter += 1

        bouncy_prop = 100*bouncy_counter/n
        print(f"{n}: bouncy proportion {bouncy_counter}/{n}= {bouncy_prop:.4f}%")
        n += 1

    print(bouncy_prop)

if __name__ == '__main__':
    solution()
