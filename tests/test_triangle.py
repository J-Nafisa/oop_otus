from scr.Triangle import Triangle
import pytest

valid_sides = [
    (3, 4, 5),
    (6, 8, 10),
]

invalid_sides = [
    (0, 1, 2),
    (1, -2, 3),
    (1, 2, 4),
    (1, 5, 2)
]

@pytest.mark.parametrize("a, b, c", valid_sides)
def test_valid_triangle_sides(a, b, c):
    # act
    triangle = Triangle(a, b, c)

    # assert
    assert triangle.a == a
    assert triangle.b == b
    assert triangle.c == c

@pytest.mark.parametrize("a, b, c", invalid_sides)
def test_invalid_triangle_sides(a, b, c):
    # act/assert
    with pytest.raises(ValueError):
        triangle = Triangle(a, b, c)

@pytest.mark.parametrize("a, b, c", valid_sides)
def test_triangle_perimeter(a, b, c):
    # arrange
    expected_perimeter = a + b + c

    # act
    triangle = Triangle(a, b, c)

    # assert
    assert triangle.perimeter == expected_perimeter


@pytest.mark.parametrize("a, b, c", valid_sides)
def test_triangle_area(a, b, c):
    # arrange
    per = (a + b + c) / 2
    expected_area = (per * (per - a) * (per - b) * (per - c)) ** 0.5

    # act
    triangle = Triangle(a, b, c)

    # assert
    assert triangle.area == pytest.approx(expected_area)

@pytest.mark.parametrize("a, b, c", invalid_sides)
def test_invalid_triangle_creation(a, b, c):
        # act/assert
        with pytest.raises(ValueError):
            triangle = Triangle(a, b, c)