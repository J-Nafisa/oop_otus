import math
from scr.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError(f"Invalid value for radius of circle: {radius} (should be positive)")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
