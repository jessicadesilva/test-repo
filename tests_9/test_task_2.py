import pytest
import numpy as np
from PIL import Image
import pytest_mpl

import task_2


def test_import_numpy():
    try:
        task_2.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


def test_import_plt():
    try:
        task_2.plt
    except AttributeError:
        pytest.fail("matplotlib.pyplot not imported as plt")


def test_import_image():
    try:
        task_2.Image
    except AttributeError:
        pytest.fail("Image not imported from PIL")


def test_image_array():
    (
        np.testing.assert_almost_equal(
            task_2.image,
            np.array(Image.open("image.png").convert("L")),
            err_msg="Image not converted to grayscale numpy array correctly.",
        ),
    )


def test_svd():
    U, S, Vt = np.linalg.svd(np.array(Image.open("image.png").convert("L")))
    np.testing.assert_almost_equal(task_2.U, U, err_msg="U matrix not as expected.")
    np.testing.assert_almost_equal(task_2.S, S, err_msg="S matrix not as expected.")
    np.testing.assert_almost_equal(task_2.Vt, Vt, err_msg="Vt matrix not as expected.")


@pytest.mark.parametrize(
    "U, S, Vt, num_singular_values, expected",
    [
        # Test case 1: 3x3 matrix, retain 1 singular value
        (
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),  # U
            np.array([5, 4, 3], dtype=float),  # S
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),  # Vt
            1,  # num_singular_values
            np.array(
                [[5.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
            ),  # expected output of compressed image
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
            2,  # num_singular_values
            np.array(
                [
                    [7.0, 0.0, 0.0, 0.0],
                    [0.0, 6.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0],
                ]
            ),  # expected output of compressed image
        ),
        # Test case 3: Non-square matrix, retain 2 singular values
        (
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]], dtype=float),  # U
            np.array([7, 6, 5], dtype=float),  # S
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float),  # Vt
            3,  # num_singular_values
            np.array(
                [[7.0, 0.0, 0.0], [0.0, 6.0, 0.0], [0.0, 0.0, 5.0], [0.0, 0.0, 0.0]]
            ),  # expected output of compressed image
        ),
    ],
)
def test_compress_image(U, S, Vt, num_singular_values, expected):
    # Call the compress_image function
    compressed_image = task_2.compress_image(U, S, Vt, num_singular_values)

    # Check if the output of the compressed image matches the expected output
    (
        np.testing.assert_almost_equal(
            compressed_image,
            expected,
            err_msg=f"\n\nInput: compress_image({U}, {S}, {Vt}, {num_singular_values})\nExpected output: {expected}\n\n",
        ),
    )


@pytest.mark.mpl_image_compare
def test_plot_svd_comparison():
    fig = task_2.plot_svd_comparison(
        task_2.compressed_image_5,
        task_2.compressed_image_10,
        task_2.compressed_image_30,
        task_2.compressed_image_50,
        task_2.compressed_image_100,
        task_2.image,
    )
    return fig
