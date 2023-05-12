from Figure import Figure

class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError(f"Invalid value for side: {side} (should be positive)")
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return 4 * self.side

