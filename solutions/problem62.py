import math
import collections
from euler_lib import numbers as nums

def solution():
    digits2cubes = collections.defaultdict(list)
    perms_count = 0
    cube_index = 10
    N = 5
    while perms_count < N:
        cube = cube_index**3
        digits = "".join([str(d) for d in sorted(nums.num_to_digitlist(cube))])
        digits2cubes[digits].append(cube)
        perms_count = len(digits2cubes[digits])
        if perms_count == N:
            print("cube permutations")
            print(digits2cubes[digits])
            smallest_cube = min(digits2cubes[digits])
            print(smallest_cube)
        cube_index += 1

    # print(digits2cubes)


if __name__ == '__main__':
    solution()
