import pytest
import task_2

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 3, 4], 24),
        ([2, 3, 5], 30),
        ([10], 10),
        ([1, 1, 1], 1),
    ],
)
def test_product_list(input_list:list, expected:float) -> None:
    assert (
        task_2.product_list(input_list) == expected
    ), f"\n\nInput: product_list({input_list})\nExpected output: {expected}\n\n"

@pytest.mark.parametrize(
    "input, expected",
    [
        (3, 14),
        (5, 55),
        (1, 1),
        (0, 0),
    ],
)
def test_sum_of_squares(input:int, expected:int) -> None:
    assert (
        task_2.sum_of_squares(input) == expected
    ), f"\n\nInput: sum_of_squares({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        (3, 6),
        (5, 120),
        (1, 1),
    ],
)
def test_factorial(input:int, expected:int) -> None:
    assert (
        task_2.factorial(input) == expected
    ), f"\n\nInput: factorial({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "a, d, n, expected",
    [
        (1, 1, 5, 15),
        (2, 2, 3, 12),
        (1, 0, 4, 4),
        (3, -1, 3, 6),
    ],
)
def test_arithmetic_series(a:float, d:float, n:int, expected:float) -> None:
    assert (
        task_2.arithmetic_series(a, d, n) == expected
    ), f"\n\nInput: arithmetic_series({a}, {d}, {n})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "a, r, n, expected",
    [
        (1, 2, 3, 7),
        (2, 3, 2, 8),
        (1, 1, 4, 4),
        (3, 0, 3, 3),
    ],
)
def test_geometric_series(a:float, r:float, n:int, expected:float) -> None:
    assert (
        task_2.geometric_series(a, r, n) == expected
    ), f"\n\nInput: geometric_series({a}, {r}, {n})\nExpected output: {expected}\n\n"
