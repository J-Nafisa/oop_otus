import math
import pytest
from scr.Circle import Circle
from scr.Rectangle import Rectangle
from scr.Square import Square
from scr.Triangle import Triangle


def test_add_area_rectangle_square():
    rectangle = Rectangle(2, 5)
    square = Square(3)
    assert rectangle.add_area(square) == 19


def test_add_area_square_circle():
    square = Square(4)
    circle = Circle(7)
    assert square.add_area(circle) == pytest.approx(85.539)


def test_add_area_circle_triangle():
    circle = Circle(6)
    triangle = Triangle(5, 12, 13)
    assert circle.add_area(triangle) == pytest.approx(113)


if __name__ == "__main__":
    pytest.main()




