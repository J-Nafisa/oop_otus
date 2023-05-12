import pytest
from scr.Circle import Circle
from scr.Rectangle import Rectangle
from scr.Square import Square
from scr.Triangle import Triangle

def test_add_area_rectangle_square():
    rectangle = Rectangle(5, 10)
    square = Square(4)
    assert rectangle.add_area(square) == 66

def test_add_area_square_circle():
    square = Square(4)
    circle = Circle(10)
    assert square.add_area(circle) == pytest.approx(502.6548245743669)

def test_add_area_circle_triangle():
    circle = Circle(10)
    triangle = Triangle(3, 4, 5)
    assert circle.add_area(triangle) == pytest.approx(306.2831853071796)





