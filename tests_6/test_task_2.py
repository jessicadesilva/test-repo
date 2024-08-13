import pytest

import task_2


def test_import_plt():
    try:
        task_2.plt
    except AttributeError:
        pytest.fail("matplotlib.pyplot not imported")


def test_import_f():
    try:
        task_2.f
    except AttributeError:
        pytest.fail("f from task_1 not imported")


def test_import_true_y():
    try:
        task_2.true_y
    except AttributeError:
        pytest.fail("true_y from task_1 not imported")


def test_runge_kutta_2_basic():
    # Test with a simple linear ODE dy/dt = y
    def f(t, y):
        return y

    t0 = 0
    y0 = 1
    t_end = 1
    h = 0.1

    t_values, y_values = task_2.runge_kutta_2(f, t0, y0, t_end, h)

    expected_t_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    expected_y_values = [
        1.0,
        1.105,
        1.221025,
        1.349232625,
        1.490902050625,
        1.647446765940625,
        1.8204286763643904,
        2.0115736873826515,
        2.22278892455783,
        2.456181761636402,
        2.714080846608224,
    ]

    assert t_values == pytest.approx(
        expected_t_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,1], h=0.1\nt_values not as expected\n\n"
    assert y_values == pytest.approx(
        expected_y_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,1], h=0.1\ny_values not as expected\n\n"


def test_runge_kutta_2_step_size():
    # Test with different step sizes
    def f(t, y):
        return -2 * t * y

    t0 = 0
    y0 = 1
    t_end = 1

    # Testing with a larger step size
    h_large = 0.5
    t_values_large, y_values_large = task_2.runge_kutta_2(f, t0, y0, t_end, h_large)
    expected_t_values_large = [0.0, 0.5, 1.0]
    expected_y_values_large = [1.0, 0.75, 0.375]

    assert t_values_large == pytest.approx(
        expected_t_values_large, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.5\nt_values not as expected\n\n"
    assert y_values_large == pytest.approx(
        expected_y_values_large, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.5\ny_values not as expected\n\n"

    # Testing with a smaller step size
    h_small = 0.1
    t_values_small, y_values_small = task_2.runge_kutta_2(f, t0, y0, t_end, h_small)
    expected_t_values_small = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    expected_y_values_small = [
        1.0,
        0.99,
        0.960696,
        0.9138140352,
        0.85204020642048,
        0.778764748668319,
        0.697773214806814,
        0.612923991886305,
        0.527850141812486,
        0.445716659746463,
        0.369053394270071,
    ]

    assert t_values_small == pytest.approx(
        expected_t_values_small, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.1\nt_values not as expected\n\n"
    assert y_values_small == pytest.approx(
        expected_y_values_small, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.1\ny_values not as expected\n\n"


def test_runge_kutta_2_edge_case():
    # Test edge case with zero step size (should raise an error or behave correctly)
    def f(t, y):
        return y

    t0 = 0
    y0 = 1

    # Test with t_end equal to t0
    t_end = t0
    h = 0.1

    t_values, y_values = task_2.runge_kutta_2(f, t0, y0, t_end, h)
    expected_t_values = [0.0]
    expected_y_values = [1.0]

    assert t_values == pytest.approx(
        expected_t_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,0], h=0.1\nt_values not as expected\n\n"
    assert y_values == pytest.approx(
        expected_y_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,0], h=0.1\ny_values not as expected\n\n"


@pytest.mark.mpl_image_compare
def test_plot_runge_kutta_2():
    return task_2.plot_runge_kutta_2(
        task_2.f, 0, 1, 2, [0.2, 0.1, 0.05, 0.01, 0.001], task_2.true_y
    )
