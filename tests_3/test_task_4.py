import pytest
import task_4


@pytest.mark.parametrize(
    "input, expected",
    [
        (-2, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (10, False),
    ],
)
def test_is_prime(input: int, expected: bool) -> None:
    assert (
        task_4.is_prime(input) == expected
    ), f"\n\nInput: is_prime({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 5),
        (10, 34),
    ],
)
def test_fibonacci(input: int, expected: int) -> None:
    assert (
        task_4.fibonacci(input) == expected
    ), f"\n\nInput: fibonacci({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, [2]),
        (2, [2, 3]),
        (3, [2, 3, 5]),
        (4, [2, 3, 5, 13]),
        (5, [2, 3, 5, 13, 89]),
    ],
)
def test_prime_fibonacci(input: int, expected: list) -> None:
    assert (
        task_4.prime_fibonacci(input) == expected
    ), f"\n\nInput: prime_fibonacci({input})\nExpected output: {expected}\n\n"
