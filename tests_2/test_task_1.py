import pytest
import task_1


@pytest.mark.parametrize(
    "input, expected",
    (
        (0, 3),
        (1, 5),
        (-1, 1),
        (2, 7),
    ),
)
def test_linear_function(input: float, expected: float) -> None:
    assert (
        task_1.linear_function(input) == expected
    ), f"\n\nInput: linear_function({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    (
        (0, 4),
        (10, 4),
        (-5, 4),
        (0.5, 4),
    ),
)
def test_constant_function(input: float, expected: float) -> None:
    assert (
        task_1.constant_function(input) == expected
    ), "\n\nInput: constant_function({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    (
        (0, 1),
        (1, 2),
        (2, 4),
        (-1, 0.5),
    ),
)
def test_exponential_function(input: float, expected: float) -> None:
    assert (
        task_1.exponential_function(input) == expected
    ), f"\n\nInput: exponential_function({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    (
        (0, 0),
        (1, 1),
        (-1, 1),
        (2.5, 2.5),
        (-2.5, 2.5),
    ),
)
def test_absolute_value(input: float, expected: float) -> None:
    assert (
        task_1.absolute_value(input) == expected
    ), f"\n\nInput: absolute_value({input})\nExpected output: {expected}\n\n"
