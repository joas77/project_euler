import math
def area(base, side):
    return (base/4) * math.sqrt(4*side*side - base*base)

N = 1_000_000_000
#N = 1_000_000_000

perimeters_sum = 0
for side in range(2,N//3+1):
    area1 = area(side+1, side)
    area2 = area(side-1, side)
    if area1.is_integer():
        # print(f"triangle, {side}, {side}, {side+1} and A = {area1} is almost equilateral")
        perimeters_sum += 2*side + side + 1
    if area2.is_integer():
        # print(f"triangle, {side}, {side}, {side-1} and A = {area2} is almost equilateral")
        perimeters_sum += 2*side + side - 1

print(f"solution: {perimeters_sum}")
