import math
import pytest
from scr.Square import Square

@pytest.mark.parametrize("side", [2, 5, 10])
def test_square_properties(side):
    # arrange
    square = Square(side)

    # act
    calculated_perimeter = square.perimeter
    calculated_area = square.area

    # assert
    expected_perimeter = 4 * side
    expected_area = side ** 2
    assert calculated_perimeter == expected_perimeter
    assert calculated_area == expected_area


@pytest.mark.parametrize("side", [-1, 0])
def test_invalid_square_creation(side):
    # arrange/act/assert
    with pytest.raises(ValueError):
        Square(side)


def test_square_equivalence():
    # arrange
    side = 5
    square1 = Square(side)
    square2 = Square(side)

    # act/assert
    assert square1.side == square2.side
    assert square1.area == square2.area
    assert square1.perimeter == square2.perimeter
