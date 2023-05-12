import math
import pytest
from scr.Circle import Circle


@pytest.mark.parametrize("radius", [2, 5, 10])
def test_circle_properties(radius):
    # arrange
    circle = Circle(radius)

    # act
    calculated_perimeter = circle.perimeter
    calculated_area = circle.area

    # assert
    expected_perimeter = 2 * math.pi * radius
    expected_area = math.pi * radius**2
    assert calculated_perimeter == expected_perimeter
    assert calculated_area == expected_area


@pytest.mark.parametrize("radius", [-1, 0])
def test_invalid_circle_creation(radius):
    # arrange/act/assert
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_equivalence():
    # arrange
    radius = 5
    circle1 = Circle(radius)
    circle2 = Circle(radius)

    # act/assert
    assert circle1.radius == circle2.radius

    # Check area
    assert math.isclose(circle1.area, circle2.area, rel_tol=1e-5)

    # Check perimeter
    assert math.isclose(circle1.perimeter, circle2.perimeter, rel_tol=1e-5)
