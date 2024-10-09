import pytest
import math

import task_1

def test_import_plt():
    try:
        task_1.plt.rcdefaults()
    except AttributeError:
        pytest.fail("matplotlib.pyplot not imported")


def test_import_math():
    try:
        task_1.math
    except AttributeError:
        pytest.fail("math not imported")

def test_eulers_method_basic():
    # Test with a simple linear ODE dy/dt = y
    def f(t, y):
        return y

    t0 = 0
    y0 = 1
    t_end = 1
    h = 0.1

    t_values, y_values = task_1.eulers_method(f, t0, y0, t_end, h)

    expected_t_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    expected_y_values = [
        1.0,
        1.1,
        1.21,
        1.331,
        1.4641,
        1.61051,
        1.771561,
        1.9487171,
        2.14358881,
        2.357947691,
        2.5937424601,
    ]

    assert t_values == pytest.approx(
        expected_t_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,1], h=0.1\nt_values not as expected\n\n"
    assert y_values == pytest.approx(
        expected_y_values, rel=1e-6
    ), "\n\nInput: dy/dx = y, y(0)=1, [0,1], h=0.1\ny_values not as expected\n\n"


def test_eulers_method_step_size():
    # Test with different step sizes
    def f(t, y):
        return -2 * t * y

    t0 = 0
    y0 = 1
    t_end = 1

    # Testing with a larger step size
    h_large = 0.5
    t_values_large, y_values_large = task_1.eulers_method(f, t0, y0, t_end, h_large)
    expected_t_values_large = [0.0, 0.5, 1.0]
    expected_y_values_large = [1.0, 1, 0.5]

    assert t_values_large == pytest.approx(
        expected_t_values_large, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.5\nt_values not as expected\n\n"
    assert y_values_large == pytest.approx(
        expected_y_values_large, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.5\ny_values not as expected\n\n"

    # Testing with a smaller step size
    h_small = 0.1
    t_values_small, y_values_small = task_1.eulers_method(f, t0, y0, t_end, h_small)
    expected_t_values_small = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    expected_y_values_small = [
        1.0,
        1.0,
        0.98,
        0.9408,
        0.884352,
        0.81360384,
        0.732243456,
        0.64437424128,
        0.5541618475008,
        0.465495951900672,
        0.381706680558551,
    ]

    assert t_values_small == pytest.approx(
        expected_t_values_small, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.1\nt_values not as expected\n\n"
    assert y_values_small == pytest.approx(
        expected_y_values_small, rel=1e-6
    ), "\n\nInput: dy/dx = -2ty, y(0)=1, [0,1], h=0.1\ny_values not as expected\n\n"

def f(t, y):
    return -2 * t * y


@pytest.mark.parametrize(
    "t, y, expected",
    [
        (1, 2, -4),
        (0, 3, 0),
        (-1, -2, -4),
        (1000, 1000, -2000000),
        (0.5, 0.1, -0.1),
    ],
)
def test_f(t, y, expected):
    assert (
        task_1.f(t, y) == expected
    ), f"\n\nInput: f({t}, {y})\nExpected output: {expected}\n\n"


@pytest.mark.parametrize(
    "t, expected",
    [
        (0, 1),
        (1, 0.36787944117),
        (-1, 0.36787944117),
        (2, 0.01831563888),
        (0.5, 0.77880078307),
    ],
)
def test_true_y(t, expected):
    assert task_1.true_y(t) == pytest.approx(
        expected
    ), f"\n\nInput: true_y({t})\nExpected output: {expected}\n\n"


def f(t, y):
    return -2 * t * y


def true_y(t):
    math.e ** (-(t**2))


@pytest.mark.mpl_image_compare
def test_plot_eulers_method():
    return task_1.plot_eulers_method(f, 0, 1, 2, [0.2, 0.1, 0.05, 0.01, 0.001], true_y)
