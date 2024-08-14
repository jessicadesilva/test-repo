import pytest
import numpy as np
import task_1


def test_import_numpy():
    try:
        task_1.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


def test_A():
    assert np.array_equal(
        task_1.A, np.array([[4, 3], [1, 3]])
    ), "Matrix A not initialized correctly"


def test_eigenvalues():
    (
        np.testing.assert_almost_equal(
            task_1.eigenvalues,
            np.array([(7 + 13 ** (0.5)) / 2, (7 - 13 ** (0.5)) / 2]),
            err_msg=f"Eigenvalues of {task_1.A} not correct.",
        ),
    )


def test_eigenvectors_as_cols():
    (
        np.testing.assert_almost_equal(
            task_1.eigenvectors_as_cols,
            np.array([[0.917246, -0.793252], [0.398322, 0.608894]]),
            decimal=5,
            err_msg=f"Column version of eigenvectors of {task_1.A} not correct.",
        ),
    )


def test_eigenvectors():
    (
        np.testing.assert_almost_equal(
            task_1.eigenvectors,
            np.array([[0.917246, 0.398322], [-0.793252, 0.608894]]),
            decimal=5,
            err_msg=f"List version of eigenvectors of {task_1.A} not correct.",
        ),
    )


@pytest.mark.parametrize(
    "A, eigenvalues, eigenvectors, expected",
    [
        # Test case 1: Diagonal matrix (eigenvectors are standard basis vectors)
        (
            np.array([[2, 0], [0, 3]]),
            np.array([2, 3]),
            [np.array([1, 0]), np.array([0, 1])],
            True,
        ),
        # Test case 2: Symmetric matrix (eigenvalues are real)
        (
            np.array([[1, 2], [2, 1]]),
            np.array([3, -1]),
            [np.array([1, 1]) / np.sqrt(2), np.array([1, -1]) / np.sqrt(2)],
            True,
        ),
        # Test case 4: Invalid eigenvector for the given matrix
        (
            np.array([[1, 2], [3, 4]]),
            np.array([5, -1]),
            [np.array([1, 1]), np.array([1, 1])],
            False,
        ),
    ],
)
def test_check_eigensystem(A, eigenvalues, eigenvectors, expected):
    assert (
        task_1.check_eigensystem(A, eigenvalues, eigenvectors) == expected
    ), f"\n\nInput: check_eigensystem({A}, {eigenvalues}, {eigenvectors})\nExpected output: {expected}\n\n"
