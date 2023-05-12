class Figure:
    def __init__(self, name):
        self.name = name

    @property
    def area(self):
        raise NotImplementedError("Subclasses must implement area method.")

    @property
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method.")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The argument must be an instance of Figure.")
        return self.area + figure.area


