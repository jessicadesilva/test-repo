import pytest
import task_1


@pytest.mark.parametrize(
    "input, expected",
    (
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
    ),
)
def test_is_even(input: int, expected: bool) -> None:
    assert (
        task_1.is_even(input) == expected
    ), f"\n\nInput: is_even({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input_1, input_2, expected",
    (
        (1, 2, 2),
        (5, 3, 5),
        (-1, -2, -1),
        (0, 0, 0),
    ),
)
def test_max_of_two(input_1: float, input_2: float, expected: float) -> None:
    assert (
        task_1.max_of_two(input_1, input_2) == expected
    ), f"\n\nInput: max_of_two({input_1}, {input_2})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    (
        ("a", True),
        ("e", True),
        ("i", True),
        ("o", True),
        ("u", True),
        ("b", False),
        ("z", False),
        ("Z", False),
        ("A", True),
        ("E", True),
        ("I", True),
        ("O", True),
        ("U", True),
    ),
)
def test_is_vowel(input: str, expected: bool) -> None:
    assert (
        task_1.is_vowel(input) == expected
    ), f"\n\nInput: is_vowel({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    (
        (10, "Positive"),
        (-5, "Negative"),
        (0, "Zero"),
        (-0.5, "Negative"),
        (0.1, "Positive"),
    ),
)
def test_sign_of_number(input: float, expected: str) -> None:
    assert (
        task_1.sign_of_number(input) == expected
    ), f"\n\nInput: sign_of_number({input})\nExpected output: {expected}\n\n"
