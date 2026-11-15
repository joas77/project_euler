import math
from dataclasses import dataclass
import turtle

class Vect2d(turtle.Vec2D):
    def __init__(self, x, y):
        self.x = self[0]
        self.y = self[1]

    def rotate(self, angle):
        r = super().rotate(angle)
        return Vect2d(r[0], r[1])

    def __add__(self, other):
        res = super().__add__(other)
        return Vect2d(res[0], res[1])

    def __sub__(self, other):
        res = super().__sub__(other)
        return Vect2d(res[0], res[1])

   #  def __mul__(self, other):
   #      res = super().__mul__(other)
   #      return Vect2d(res[0], res[1])

    def __neg__(self):
        res = super().__neg__()
        return Vect2d(res[0], res[1])

class Line:
    def __init__(self, p1: Vect2d, p2: Vect2d):
        self._m = 0
        self._direction: Vect2d = p2 - p1
        dx = p2.x - p1.x

        if dx != 0:
            self._m = (p2.y - p1.y) / dx
            self._b = p1.y - self._m * p1.x
        else:
            self._m = math.inf
            self._x = p1.x

    def y(self, x:float) -> float:
        return self._m * x + self._b

    @property
    def slope(self):
        return self._m

    @property
    def b(self):
        # TODO: raise error if m = inf
        return self._b

    @staticmethod
    def point_slope(p: Vect2d, m: float) -> Line:
        # TODO : case when m = inf (vertical line)
        dx = 10
        dy = m * dx
        return Line(p, Vect2d(p.x+dx, p.y+dy))

    def direction_vector(self):
        return self._direction

    def __repr__(self):
        return f"y = {self.slope}x + ({self._b})"

    def __eq__(self, l:Line):
        if self.slope() == l.slope():
            if self.slope() != math.inf:
                return self._b == l._b
            else:
                return self._x == l._x

        return False


def lines_angle(l1: Line, l2: Line):
    u = l1.direction_vector()
    v = l2.direction_vector()
    angle = math.acos( u*v/(abs(u)*abs(v)) )
    if angle >= math.pi/2:
        angle = math.pi - angle
    return math.degrees(angle)

def elipse_slope(point: Vect2d):
    return -4*point.x/point.y

def elipse(x):
    y1 = math.sqrt(100 - 4*x*x)
    y2 = - y1
    return (y1, y2)

def solve_line_elipse(point: Vect2d, line: Line) -> Vect2d:
    A = 4 + line.slope**2
    B = 2 * line.slope * line.b
    C = line.b**2 - 100

    D = math.sqrt(B**2 - 4 * A * C)
    x1 = (-B + D)/(2*A)
    x2 = (-B - D)/(2*A)

    # using the other cross point
    x_sol = x1 if not f_equal(x1, point.x) else x2
    y1, y2 = elipse(x_sol)
    y_sol = y1 if f_equal(y1, line.y(x_sol)) else y2

    return Vect2d(x_sol, y_sol)

def f_equal(x:float, y:float, eps:float =0.00001) -> bool:
    return x - eps <= y <= x + eps

def draw_beam(pos:Vect2d):
    turtle.goto(30*pos)

def print_beam_line(l: Line):
    print(f"beam line: {l}")

def print_tangent(l: Line):
    print(f"tangent line: {l}")

def bounce_beam():
    start = Vect2d(0, 10.1)
    cross_point = Vect2d(1.4, -9.6)
    draw_beam(start)
    draw_beam(cross_point)

    l = Line(start, cross_point)
    print(f"start point: {start}")
    print_beam_line(l)
    print(f"cross point: {cross_point}")

    while True:

        m = elipse_slope(cross_point)
        tangent = Line.point_slope(cross_point, m)
        print_tangent(tangent)
        incident_angle = lines_angle(l, tangent)
        print(f"incident angle --> {incident_angle} ")
        reflection_vector = tangent.direction_vector().rotate(-incident_angle)
        reflection_line = Line(cross_point, cross_point + reflection_vector)

        print_beam_line(reflection_line)
        cross_point = solve_line_elipse(cross_point, reflection_line)
        draw_beam(cross_point)
        print(f"cross point -> {cross_point}")
        print("="*20)
        yield

def solution():
    for _ in bounce_beam():
        prompt = input()
        if prompt == "q":
            break

if __name__ == "__main__":
    solution()
