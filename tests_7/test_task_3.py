import pytest
import numpy as np

import task_3


def test_import_numpy():
    try:
        task_3.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


@pytest.mark.parametrize(
    "A, expected_L, expected_U",
    [
        (
            np.array([[4, 3], [6, 3]], dtype=float),
            np.array([[1, 0], [1.5, 1]], dtype=float),
            np.array([[4, 3], [0, -1.5]], dtype=float),
        ),
        (
            np.array([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]], dtype=float),
            np.array([[1, 0, 0], [-2, 1, 0], [-2, -1, 1]], dtype=float),
            np.array([[2, -1, -2], [0, 4, -1], [0, 0, 3]], dtype=float),
        ),
    ],
)
def test_lu_decomposition(A, expected_L, expected_U):
    L, U = task_3.lu_decomposition(A)
    np.testing.assert_array_almost_equal(L, expected_L, decimal=4)
    (
        np.testing.assert_array_almost_equal(
            U,
            expected_U,
            decimal=4,
            err_msg=f"\n\nInput: lu_decomposition({A})\nExpected output: L = {expected_L}, U = {expected_U}\n\n",
        )
    )


@pytest.mark.parametrize(
    "L, b, expected",
    [
        (
            np.array([[1, 0], [0.5, 1]], dtype=float),
            np.array([2, 1], dtype=float),
            np.array([2, 0], dtype=float),
        ),
        (
            np.array([[1, 0, 0], [-2, 1, 0], [-1, 2, 1]], dtype=float),
            np.array([1, 0, 3], dtype=float),
            np.array([1, 2, 0], dtype=float),
        ),
    ],
)
def test_forward_substitution(L, b, expected):
    y = task_3.forward_substitution(L, b)
    (
        np.testing.assert_array_almost_equal(
            y,
            expected,
            decimal=4,
            err_msg=f"\n\nInput: forward_substitution({L}, {b})\nExpected output: {expected}\n\n",
        ),
    )


@pytest.mark.parametrize(
    "U, y, expected",
    [
        (
            np.array([[4, 3], [0, 1.5]], dtype=float),
            np.array([2, 1], dtype=float),
            np.array([0, 2 / 3], dtype=float),
        ),
        (
            np.array([[2, -1, -2], [0, 4, -1], [0, 0, 3]], dtype=float),
            np.array([1, 2, 3], dtype=float),
            np.array([15 / 8, 0.75, 1.0], dtype=float),
        ),
    ],
)
def test_backward_substitution(U, y, expected):
    x = task_3.backward_substitution(U, y)
    (
        np.testing.assert_array_almost_equal(
            x,
            expected,
            decimal=4,
            err_msg=f"\n\nInput: backward_substitution({U}, {y})\nExpected output: {expected}\n\n",
        ),
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
def test_solve_lu(A, b, expected):
    x = task_3.solve_lu(A, b)
    (
        np.testing.assert_array_almost_equal(
            x,
            expected,
            decimal=4,
            err_msg=f"\n\nInput: solve_lu({A}, {b})\nExpected output: {expected}\n\n",
        )
    )
