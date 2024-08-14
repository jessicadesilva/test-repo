import pytest
import numpy as np

import task_3


def test_import_numpy():
    try:
        task_3.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


@pytest.mark.parametrize(
    "A, expected_Q, expected_R",
    [
        # Test with a simple 2x2 matrix.
        (
            np.array([[1, 2], [3, 4]], dtype=float),
            np.array([[0.31622777, 0.9486833], [0.9486833, -0.31622777]]),
            np.array(
                [[3.16227766e00, 4.42718872e00], [-1.05471187e-15, 6.32455532e-01]]
            ),
        ),
        # Test with a 3x3 matrix.
        (
            np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], dtype=float),
            np.array(
                [
                    [0.89442719, 0.35856858, 0.26726124],
                    [-0.4472136, 0.71713717, 0.53452248],
                    [0.0, -0.5976143, 0.80178373],
                ]
            ),
            np.array(
                [
                    [2.23606798e00, -1.78885438e00, 4.47213595e-01],
                    [-2.22044605e-16, 1.67332005e00, -1.91236577e00],
                    [-3.33066907e-16, 0.00000000e00, 1.06904497e00],
                ]
            ),
        ),
        # Test with a 4x4 matrix.
        (
            np.array(
                [[7, 4, 8, 2], [4, 5, 8, 3], [8, 8, 4, 9], [2, 3, 9, 8]],
                dtype=float,
            ),
            np.array(
                [
                    [0.60697698, -0.72453803, 0.32222144, -0.05288599],
                    [0.34684399, 0.47563211, 0.29244179, -0.75362533],
                    [0.69368798, 0.29572981, -0.59672029, 0.27434606],
                    [0.17342199, 0.40169966, 0.67422254, 0.59496737],
                ]
            ),
            np.array(
                [
                    [11.53256259, 10.23189764, 11.96611758, 9.88505365],
                    [0.0, 3.05094587, 2.80696877, 5.85298581],
                    [0.0, 0.0, 8.59842755, 1.54506591],
                    [0.0, 0.0, 0.0, 4.86220554],
                ]
            ),
        ),
    ],
)
def test_qr_decomposition(A, expected_Q, expected_R):
    Q, R = task_3.qr_decomposition(A)

    np.testing.assert_almost_equal(
        Q,
        expected_Q,
        err_msg=f"\n\nInput: qr_decomposition({A})\nExpected Q: {expected_Q}",
    )

    np.testing.assert_almost_equal(
        R,
        expected_R,
        err_msg=f"\n\nInput: qr_decomposition({A})\nExpected R: {expected_R}",
    )


@pytest.mark.parametrize(
    "A, expected",
    [
        # Test with a simple 2x2 matrix.
        (
            np.array([[1, 2], [3, 4]], dtype=float),
            np.array([5.37228132, -0.37228132]),
        ),
        # Test with a 3x3 matrix.
        (
            np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], dtype=float),
            np.array([3.41421356, 2.0, 0.58578644]),
        ),
        # Test with a 4x4 matrix.
        (
            np.array(
                [[7, 4, 8, 2], [4, 5, 8, 3], [8, 8, 4, 9], [2, 3, 9, 8]],
                dtype=float,
            ),
            np.array([23.43261567, -6.76313861, 5.70293116, 1.62759177]),
        ),
    ],
)
def test_qr_algorithm(A, expected):
    eigenvalues = task_3.qr_algorithm(A, 100)

    np.testing.assert_almost_equal(
        eigenvalues,
        expected,
        err_msg=f"\n\nInput: qr_algorithm({A}, 1000)\nExpected: {expected}",
    )
