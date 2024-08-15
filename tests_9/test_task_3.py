import pytest
import numpy as np
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

import task_3


def test_import_numpy():
    try:
        task_3.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


def test_import_plt():
    try:
        task_3.plt
    except AttributeError:
        pytest.fail("matplotlib.pyplot not imported as plt")


def test_import_load_wine():
    try:
        task_3.load_wine()
    except AttributeError:
        pytest.fail("load_wine not imported from sklearn.datasets")


def test_import_StandardScalar():
    try:
        task_3.StandardScaler()
    except AttributeError:
        pytest.fail("StandardScaler not imported from sklearn.preprocessing")


def test_X():
    np.testing.assert_almost_equal(
        task_3.X, load_wine().data, err_msg="Variable X not initialized correctly"
    )


def test_y():
    np.testing.assert_almost_equal(
        task_3.y, load_wine().target, err_msg="Variable y not initialized correctly"
    )


def test_X_standardized():
    np.testing.assert_almost_equal(
        task_3.X_standardized,
        StandardScaler().fit_transform(load_wine().data),
        err_msg="X_standardized is not defined correctly",
    )


def test_svd():
    U, S, Vt = np.linalg.svd(StandardScaler().fit_transform(load_wine().data))
    np.testing.assert_almost_equal(task_3.U, U, err_msg="Variable U in SVD not correct")
    np.testing.assert_almost_equal(task_3.S, S, err_msg="Variable S in SVD not correct")
    np.testing.assert_almost_equal(
        task_3.Vt, Vt, err_msg="Variable Vt in SVD not correct"
    )


@pytest.mark.parametrize(
    "U, S, Vt, num_dimensions, expected",
    [
        # Test case 1: 3x3 matrix, retain 1 singular value
        (
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),  # U
            np.array([5, 4, 3], dtype=float),  # S
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),  # Vt
            1,  # num_dimensions
            np.array(
                [[5.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
            ),  # expected output of reduced data
        ),
        # Test case 2: 4x4 matrix, retain 2 singular values
        (
            np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float
            ),  # U
            np.array([7, 6, 5, 4], dtype=float),  # S
            np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float
            ),  # Vt
            2,  # num_dimensions
            np.array(
                [
                    [7.0, 0.0, 0.0, 0.0],
                    [0.0, 6.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0],
                ]
            ),  # expected output of reduced data
        ),
        # Test case 3: Non-square matrix, retain 2 singular values
        (
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]], dtype=float),  # U
            np.array([7, 6, 5], dtype=float),  # S
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),  # Vt
            3,  # num_dimensions
            np.array(
                [[7.0, 0.0, 0.0], [0.0, 6.0, 0.0], [0.0, 0.0, 5.0], [0.0, 0.0, 0.0]]
            ),  # expected output of reduced data
        ),
    ],
)
def test_reduce_dimensions(U, S, Vt, num_dimensions, expected):
    # Call the reduce_dimensions function
    reduced_data = task_3.reduce_dimensions(U, S, Vt, num_dimensions)

    # Check if the output of reduced data matches the expected output
    (
        np.testing.assert_almost_equal(
            reduced_data,
            expected,
            err_msg=f"\n\nInput: reduce_dimensions({U}, {S}, {Vt}, {num_dimensions})\nExpected output: {expected}\n\n",
        ),
    )


@pytest.mark.mpl_image_compare
def test_plot_data_2D():
    fig = task_3.plot_data_2D(task_3.X_standardized, task_3.X_reduced_2, task_3.y)
    return fig


@pytest.mark.mpl_image_compare
def test_plot_data_3D():
    fig = task_3.plot_data_3D(task_3.X_standardized, task_3.X_reduced_3, task_3.y)
    return fig
