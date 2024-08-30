import pytest
import task_3


@pytest.mark.parametrize(
    "input, expected",
    (
        ([1, 2, 3], 1),
        ([1], 1),
        (["a", "b", "c"], "a"),
        ([True, False], True),
    ),
)
def test_first_element(input: list, expected) -> None:
    assert (
        task_3.first_element(input) == expected
    ), f"\n\nInput: first_element({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    (
        ([1, 2, 3], 3),
        ([1], 1),
        (["a", "b", "c"], "c"),
        ([True, False], False),
    ),
)
def test_last_element(input: list, expected) -> None:
    assert (
        task_3.last_element(input) == expected
    ), f"\n\nInput: last_element({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "input, expected",
    (
        ([1, 2, 3], 4),
        ([1], 2),
        ([4, 3, 2, -1], 3),
    ),
)
def test_first_last_sum(input: list, expected: float) -> None:
    assert (
        task_3.first_last_sum(input) == expected
    ), f"\n\nInput: first_last_sum({input})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "point, expected",
    (
        ((3, 4), 5),
        ((0, 0), 0),
        ((-3, -4), 5),
    ),
)
def test_distance_from_origin(point: tuple, expected: float) -> None:
    assert (
        task_3.distance_from_origin(point) == expected
    ), f"\n\nInput: distance_from_origin({point})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "point_1, point_2, expected",
    (
        ((1, 2), (4, 6), 5),
        ((0, 0), (0, 0), 0),
        ((-1, -1), (-4, -5), 5),
    ),
)
def test_distance_between(point_1: tuple, point_2: tuple, expected: float):
    assert (
        task_3.distance_between(point_1, point_2) == expected
    ), f"\n\nInput: distance_between({point_1}, {point_2})\nExpected output: {expected}\n\n"
