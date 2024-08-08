import pytest
import task_4


def func(x):
    return x


def test_import():
    try:
        task_4.task_3.central_difference(func, 1, 1)
    except AttributeError:
        pytest.fail("task_3 module not imported")


@pytest.mark.parametrize(
    "input, expected",
    (
        (0, 1),
        (1, 5),
        (-1, -3),
        (2, 141),
        (-2, -139),
        (3, 1141),
    ),
)
def test_example_function(input: float, expected: float) -> None:
    assert (
        task_4.example_function(input) == expected
    ), f"\n\nInput: example_function({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected", ((0, 2), (1, 18), (-1, 18), (2, 366), (3, 1946))
)
def test_true_derivative(input: float, expected: float) -> None:
    assert (
        task_4.true_derivative(input) == expected
    ), f"\n\nInput: true_derivative({input})\nExpected output: {expected}\n\n"
