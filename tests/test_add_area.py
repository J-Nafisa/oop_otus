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
    square = Square(9)
    circle = Circle(12)
    expected_result = square.area + circle.area
    tolerance = 1.1e-04
    assert square.add_area(circle) == pytest.approx(expected_result, abs=tolerance)


def test_add_area_circle_triangle():
    circle = Circle(6)
    triangle = Triangle(5, 12, 13)
    expected_result = circle.area + triangle.area
    tolerance = 1.1e-04
    assert circle.add_area(triangle) == pytest.approx(expected_result, abs=tolerance)




