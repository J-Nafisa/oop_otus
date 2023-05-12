import math
from scr.Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        if a <= 0:
            raise ValueError(f"Invalid value for side of triangle: a = {a} (should be positive)")
        elif b <= 0:
            raise ValueError(f"Invalid value for side of triangle: b = {b} (should be positive)")
        elif c <= 0:
            raise ValueError(f"Invalid value for side of triangle: c = {c} (should be positive)")
        elif c >= a + b:
            raise ValueError(f"Invalid value for side of triangle: c = {c} (should be less than a + b)")
        elif a >= b + c:
            raise ValueError(f"Invalid value for side of triangle: a = {a} (should be less than b + c)")
        elif b >= a + c:
            raise ValueError(f"Invalid value for side of triangle: b = {b} (should be less than a + c)")
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        per = self.perimeter / 2
        return math.sqrt(per * (per - self.a) * (per - self.b) * (per - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
