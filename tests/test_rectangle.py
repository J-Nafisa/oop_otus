import pytest
from scr.Rectangle import Rectangle

@pytest.mark.parametrize("width, height", [
    (4, 6),
    (7, 9),
    (10, 3)
])
def test_rectangle_properties(width, height):
    # arrange
    rectangle = Rectangle(width, height)

    # act
    calculated_perimeter = rectangle.perimeter
    calculated_area = rectangle.area

    # assert
    expected_perimeter = 2 * (width + height)
    expected_area = width * height
    assert calculated_perimeter == expected_perimeter
    assert calculated_area == expected_area


@pytest.mark.parametrize("width, height", [
    (0, 6),  # Invalid width value
    (4, -1),  # Invalid height value
    (-2, 3)  # Invalid width value
])
def test_invalid_rectangle_creation(width, height):
    # arrange/act/assert
    with pytest.raises(ValueError):
        Rectangle(width, height)


def test_rectangle_equivalence():
    # arrange
    rectangle1 = Rectangle(4, 6)
    rectangle2 = Rectangle(4, 6)

    # act/assert
    assert rectangle1.width == rectangle2.width
    assert rectangle1.height == rectangle2.height

    # Check area
    assert rectangle1.area == rectangle2.area

    # Check perimeter
    assert rectangle1.perimeter == rectangle2.perimeter
