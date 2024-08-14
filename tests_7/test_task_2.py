import pytest
import numpy as np

import task_2


def test_import_numpy():
    try:
        task_2.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


@pytest.mark.parametrize(
    "A, i, divisor, expected",
    [
        (
            np.array([[2, 4, 6], [1, 3, 5]], dtype=float),
            0,
            2,
            np.array([[1, 2, 3], [1, 3, 5]], dtype=float),
        ),
        (
            np.array([[6, 9, 12], [2, 4, 8]], dtype=float),
            1,
            2,
            np.array([[6, 9, 12], [1, 2, 4]], dtype=float),
        ),
    ],
)
def test_divide_row(A, i, divisor, expected):
    task_2.divide_row(A, i, divisor)
    (
        np.testing.assert_array_almost_equal(A, expected),
        f"\n\nInput: divide_row({A}, {i}, {divisor})\nExpected output: {expected}\n\n",
    )


@pytest.mark.parametrize(
    "A, i, j, multiplier, expected",
    [
        (
            np.array([[2, 3, -1], [4, 1, 1], [3, 2, 2]], dtype=float),
            1,
            0,
            2,
            np.array([[2, 3, -1], [0, -5, 3], [3, 2, 2]], dtype=float),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float),
            2,
            1,
            2,
            np.array([[1, 2, 3], [4, 5, 6], [-1, -2, -3]], dtype=float),
        ),
    ],
)
def test_subtract_rows(A, i, j, multiplier, expected):
    task_2.subtract_rows(A, i, j, multiplier)
    (
        np.testing.assert_array_almost_equal(A, expected),
        f"\n\nInput: subtract_rows({A}, {i}, {j}, {multiplier})\nExpected output: {expected}\n\n",
    )


@pytest.mark.parametrize(
    "A, b, expected",
    [
        (
            np.array([[2, 1], [5, 7]], dtype=float),
            np.array([11, 13], dtype=float),
            np.array([7.1111, -3.2222], dtype=float),
        ),
        (
            np.array([[1, 2, -1], [3, -1, 2], [2, 3, 1]], dtype=float),
            np.array([3, 8, 2], dtype=float),
            np.array([55 / 16, -17 / 16, -27 / 16], dtype=float),
        ),
    ],
)
def test_gauss_jordan_elimination(A, b, expected):
    result = task_2.gauss_jordan_elimination(A, b)
    (
        np.testing.assert_array_almost_equal(result, expected, decimal=4),
        f"\n\nInput: gauss_jordan_elimination({A}, {b})\nExpected output: {expected}\n\n",
    )
