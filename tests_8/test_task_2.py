import pytest
import numpy as np

import task_2


def test_import_numpy():
    try:
        task_2.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


@pytest.mark.parametrize(
    "A, num_iter, expected_eigenvalue, expected_eigenvector",
    [
        (
            np.array([[2, 0], [0, 1]]),
            10,
            1.9999999110284568,
            np.array([9.99999956e-01, 2.98280980e-04]),
        ),
        (np.array([[2, 0], [0, 1]]), 100, 2.0, np.array([1.0, 2.40949468e-31])),
        (
            np.array([[1, 2], [2, 1]]),
            5,
            2.9999808242848056,
            np.array([0.70555687, 0.7086533]),
        ),
        (np.array([[1, 2], [2, 1]]), 100, 3.0, np.array([0.70710678, 0.70710678])),
        (np.array([[3, 0, 0], [0, 2, 0], [0, 0, 1]]), 1000, 3.0, [1.0, 0.0, 0.0]),
    ],
)
def test_power_method(A, num_iter, expected_eigenvalue, expected_eigenvector):
    # Run the power method
    eigenvalue, eigenvector = task_2.power_method(A, num_iter)

    # Check if the computed eigenvalue is within the expected range
    assert (
        eigenvalue == pytest.approx(expected_eigenvalue)
    ), f"\n\nInput: power_method({A}, {num_iter})\nExpected eigenvalue: {expected_eigenvalue}\n\n"

    # Check if the eigenvector is normalized
    np.testing.assert_array_almost_equal(
        eigenvector,
        expected_eigenvector,
        err_msg=f"\n\nInput: power_method({A}, {num_iter})\nExpected eigenvector: {expected_eigenvector}\n\n",
    )


def test_import_check_eigensystem():
    try:
        task_2.check_eigensystem
    except AttributeError:
        pytest.fail("check_eigensystem from task_1 not imported")


def test_A():
    assert np.array_equal(
        task_2.A, np.array([[4, 3], [1, 3]])
    ), "Matrix A not initialized correctly"


def test_eigenvalue():
    assert (
        task_2.eigenvalue == pytest.approx(5.302775637731995)
    ), f"\n\nInput: power_method({task_2.A}, 1000)\nExpected eigenvalue: 5.302775637731995\n\n"


def test_eigenvector():
    np.testing.assert_almost_equal(
        task_2.eigenvector,
        np.array([0.91724574, 0.3983218]),
        err_msg=f"\n\nInput: power_method({task_2.A}, 1000)\nExpected eigenvalue: 5.302775637731995\n\n",
    )
