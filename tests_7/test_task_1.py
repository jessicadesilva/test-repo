import pytest
import numpy as np
import task_1


def test_import_numpy():
    try:
        task_1.np
    except AttributeError:
        pytest.fail("numpy not imported as np")


def test_v():
    assert np.array_equal(
        task_1.v, np.array([1, 2, 3])
    ), "Vector v not initialized correctly"


def test_A():
    assert np.array_equal(
        task_1.A, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ), "Matrix A not initialized correctly"


def test_v_add():
    assert np.array_equal(
        task_1.v_add, np.array([2, 4, 6])
    ), "Vector v_add not initialized correctly"


def test_v_scalar_mult():
    assert np.array_equal(
        task_1.v_scalar_mult, np.array([2, 4, 6])
    ), "Vector v_scalar_mult not initialized correctly"


def test_A_add():
    assert np.array_equal(
        task_1.A_add, np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    ), "Matrix A_add not initialized correctly"


def test_Av_mult():
    assert np.array_equal(
        task_1.Av_mult, np.array([14, 32, 50])
    ), "Vector Av_mult not initialized correctly"


def test_I():
    assert np.array_equal(
        task_1.I, np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    ), "Matrix I not initialized correctly"


def test_A_mult():
    assert np.array_equal(
        task_1.A_mult, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ), "Matrix A_mult not initialized correctly"


def test_A_transpose():
    assert np.array_equal(
        task_1.A_transpose, np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    ), "Matrix A_transpose not initialized correctly"


def test_v_norm():
    assert task_1.v_norm == pytest.approx(
        3.7416573867739413
    ), "Value v_norm not initialized correctly"
