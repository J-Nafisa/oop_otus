from Figure import Figure

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        if width <= 0:
            raise ValueError(f"Invalid value for width: {width} (should be positive)")
        if height <= 0:
            raise ValueError(f"Invalid value for height: {height} (should be positive)")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

