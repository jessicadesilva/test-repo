import pytest

import task_3


def test_import_plt():
    try:
        task_3.plt
    except AttributeError:
        pytest.fail("matplotlib.pyplot not imported")


def test_import_f():
    try:
        task_3.f
    except AttributeError:
        pytest.fail("f from task_1 not imported")


def test_import_true_y():
    try:
        task_3.true_y
    except AttributeError:
        pytest.fail("true_y from task_1 not imported")


def test_runge_kutta_4_basic():
    # Test with a simple linear ODE dy/dt = y
    def f(t, y):
        return y

    t0 = 0
    y0 = 1
    t_end = 1
    h = 0.1

    t_values, y_values = task_3.runge_kutta_4(f, t0, y0, t_end, h)

    expected_t_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    expected_y_values = [
        1.0,
        1.10517083333333,
        1.22140257085069,
        1.34985849706254,
        1.49182424008069,
        1.64872063859684,
        1.82211796209193,
        2.01375162659678,
        2.22553956329232,
        2.45960141378007,
        2.71827974413517,
    ]

    assert t_values == pytest.approx(
        expected_t_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,1], h=0.1\nt_values not as expected\n\n"
    assert y_values == pytest.approx(
        expected_y_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,1], h=0.1\ny_values not as expected\n\n"


def test_runge_kutta_4_step_size():
    # Test with different step sizes
    def f(t, y):
        return -2 * t * y

    t0 = 0
    y0 = 1
    t_end = 1

    # Testing with a larger step size
    h_large = 0.5
    t_values_large, y_values_large = task_3.runge_kutta_4(f, t0, y0, t_end, h_large)
    expected_t_values_large = [0.0, 0.5, 1.0]
    expected_y_values_large = [1.0, 0.778645833333333, 0.368031819661458]

    assert t_values_large == pytest.approx(
        expected_t_values_large, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.5\nt_values not as expected\n\n"
    assert y_values_large == pytest.approx(
        expected_y_values_large, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.5\ny_values not as expected\n\n"

    # Testing with a smaller step size
    h_small = 0.1
    t_values_small, y_values_small = task_3.runge_kutta_4(f, t0, y0, t_end, h_small)
    expected_t_values_small = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    expected_y_values_small = [
        1.0,
        0.990049833333333,
        0.960789435235578,
        0.913931174018635,
        0.852143772467446,
        0.7788007805437,
        0.697676387177754,
        0.612626609990853,
        0.527292930545312,
        0.444859036689859,
        0.367881066425765,
    ]

    assert t_values_small == pytest.approx(
        expected_t_values_small, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.1\nt_values not as expected\n\n"
    assert y_values_small == pytest.approx(
        expected_y_values_small, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.1\ny_values not as expected\n\n"


def test_runge_kutta_4_edge_case():
    # Test edge case with zero step size (should raise an error or behave correctly)
    def f(t, y):
        return y

    t0 = 0
    y0 = 1

    # Test with t_end equal to t0
    t_end = t0
    h = 0.1

    t_values, y_values = task_3.runge_kutta_4(f, t0, y0, t_end, h)
    expected_t_values = [0.0]
    expected_y_values = [1.0]

    assert t_values == pytest.approx(
        expected_t_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,0], h=0.1\nt_values not as expected\n\n"
    assert y_values == pytest.approx(
        expected_y_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,0], h=0.1\ny_values not as expected\n\n"


@pytest.mark.mpl_image_compare
def test_plot_runge_kutta_4():
    return task_3.plot_runge_kutta_4(
        task_3.f, 0, 1, 2, [0.2, 0.1, 0.05, 0.01, 0.001], task_3.true_y
    )
