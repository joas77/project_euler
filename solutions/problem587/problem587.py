import math

def x(n:int):
    a = n*n + 1
    b = 2*(1-n)
    c = 1 - 2*n

    D = math.sqrt(b*b - 4*a*c)

    x1 = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)

    return min(x1, x2)

def y(n):
    return x(n)/n + (1-n)/n

def area_left_triangle(n):
    x_n = x(n)
    return (x_n + 1)*(y(n) + 1)/2

def area_circle_section(x_n):
    return -0.5 * (x_n * math.sqrt(1 - x_n * x_n) + math.asin(x_n) )

def area_concave_triangle(n):
    x_n = x(n)
    return area_left_triangle(n) + abs(x_n) - area_circle_section(x_n)

def solution():
    p = 1
    n = 1
    while p >= 0.1:
        print(f"cross in x,y in circlefor n={n} --> {(y(n), x(n))}")
        print(f"area of circle section from {x(n):.3} to 0 = {area_circle_section(x(n)):.3}")
        print(f"area left triangle = {area_left_triangle(n)}")
        A = area_concave_triangle(n)
        print(f"area concave trianle = {A}")
        L_section = 1 - math.pi/4
        print(f"area of L section = {L_section:.3}")
        p = 100*A/L_section
        print(f"proportion: {p:.5f}%")
        print()
        n += 1



if __name__ == '__main__':
    solution()
