import pytest
import task_2

@pytest.mark.parametrize(
    "input_1, input_2, expected",
    (
        (2, 4, 3),
        (0, 0, 0),
        (-2, 2, 0),
        (1.5, -1.5, 0),
    ),
)
def test_average_value(input_1:float, input_2:float, expected:float) -> None:
    assert task_2.average_value(input_1, input_2) == expected, f"\n\nInput: average_value({input_1}, {input_2})\nExpected output: {expected}\n\n"

@pytest.mark.parametrize(
    "input_1, input_2, input_3, expected",
    (
        (1, 2, 3, 3),
        (3, 2, 1, 3),
        (-1, -2, -3, -1),
        (0, 0, 0, 0),
    ),
)
def test_max_of_three(input_1:float, input_2:float, input_3:float, expected:float) -> None:
    assert task_2.max_of_three(input_1, input_2, input_3) == expected, f"\n\nInput: max_of_three({input_1}, {input_2}, {input_3})\nExpected output: {expected}\n\n"

@pytest.mark.parametrize(
    "input_1, input_2, input_3, expected",
    (
        (1, 2, 3, 1),
        (3, 2, 1, 1),
        (-1, -2, -3, -3),
        (0, 0, 0, 0),
    ),
)
test_min_of_three(input_1:float, input_2:float, input_3:float, expected:float) -> None:
    assert task_2.min_of_three(input_1, input_2, input_3) == expected, f"\n\nInput: min_of_three({input_1}, {input_2}, {input_3})\nExpected output: {expected}\n\n"

@pytest.mark.parametrize(
    "input_1, input_2, input_3, expected",
    (
        (1, 2, 3, 2),
        (3, 2, 1, 2),
        (-1, -2, -3, -2),
        (0, 0, 0, 0),
        (2, 9, 4, 5.5),
    ),
)
def test_midrange(input_1:float, input_2:float, input_3:float, expected:float) -> None:
    assert task_2.midrange(input_1, input_2, input_3) == expected, f"\n\nInput: midrange({input_1}, {input_2}, {input_3})\nExpected output: {expected}\n\n"
