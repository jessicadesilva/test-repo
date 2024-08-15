import pytest
import numpy as np
import task_1


def test_import_numpy():
    try:
        task_1.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


@pytest.mark.parametrize(
    "input_matrix, expected",
    [
        (
            np.array([[0, 0], [0, 0]], dtype=float),
            np.array([[-0.6868784, 0.7267724], [0.7267724, 0.6868784]], dtype=float),
        ),  # 2x2 zero matrix
        (
            np.array([[1, 0], [0, 0]], dtype=float),
            np.array([[1, 0], [0, 1]], dtype=float),
        ),  # 2x2 matrix with one zero column
        (
            np.array([[1, 0], [3, 0]], dtype=float),
            np.array([[1, -0.2298364], [3, -0.9732293]], dtype=float),
        ),  # 2x2 non-zero matrix (check if it remains unchanged)
    ],
)
def test_complete_orthonormal_basis(input_matrix, expected):
    U = task_1.complete_orthonormal_basis(input_matrix.copy())
    np.testing.assert_almost_equal(
        U,
        expected,
        err_msg=f"\n\nInput: complete_orthonormal_basis({input_matrix})\nExpected output: {expected}",
    )


# Assuming the `svd` function and `complete_orthonormal_basis` function are imported from the module


@pytest.mark.parametrize(
    "A, expected_U, expected_Sigma, expected_Vt",
    [
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[-0.40455358, 0.9145143], [-0.9145143, -0.40455358]]),
            np.array([5.4649857, 0.36596619]),
            np.array([[-0.57604844, -0.81741556], [-0.81741556, 0.57604844]]),
        ),
        (
            np.array([[5, 6, 7], [8, 9, 10], [11, 12, 13]]),
            np.array(
                [
                    [-0.37299857, 0.83318989, 0.40824829],
                    [-0.55737745, 0.15054472, -0.81649658],
                    [-0.74175632, -0.53210045, 0.40824829],
                ]
            ),
            np.array([2.80818294e01, 6.40983882e-01, 6.32553041e-17]),
            np.array(
                [
                    [-0.51575458, -0.57529957, -0.63484456],
                    [-0.75321348, -0.04861828, 0.65597691],
                    [0.40824829, -0.81649658, 0.40824829],
                ]
            ),
        ),
        (np.array([[1]]), np.array([[1.0]]), np.array([1.0]), np.array([[1.0]])),
        (
            np.array([[1, 0], [0, 1]]),
            np.array([[0, 1], [1, 0]]),
            np.array([1.0, 1.0]),
            np.array([[0.0, 1.0], [1.0, 0.0]]),
        ),
    ],
)
def test_svd(A, expected_U, expected_Sigma, expected_Vt):
    # 2. Call the svd function on the matrix A and capture the output.
    U, Sigma, Vt = task_1.svd(A)

    # 5. Check if the actual values are close to the expected values.
    np.testing.assert_almost_equal(U, expected_U)
    np.testing.assert_almost_equal(Sigma, expected_Sigma)
    np.testing.assert_almost_equal(Vt, expected_Vt)
