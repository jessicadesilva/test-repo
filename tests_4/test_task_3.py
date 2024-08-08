import pytest
import task_3


def func(x):
    return 3 * x**4 - 5 * x**3 + 2 * x**2 - 7 * x + 6


def true_derivative(x):
    return 12 * x**3 - 15 * x**2 + 4 * x - 7


def test_package_import():
    try:
        task_3.plt.rcdefaults()
    except AttributeError:
        pytest.fail("matplotlib.pyplot was not imported as plt")


@pytest.mark.parametrize(
    "f, x, h, expected",
    (
        (func, 1, 0.1, -5.93),
        (func, 2, 0.5, 41.75),
    ),
)
def test_central_difference(f, x: float, h: float, expected: float) -> None:
    assert (
        task_3.central_difference(f, x, h) == pytest.approx(expected)
    ), f"\n\nInput: central_difference(f, {x}, {h}) with f(x)=3x^4-5x^3+2x^2-7x+6\nExpected output: {expected}"


def test_import():
    try:
        task_3.np.pi
    except AttributeError:
        pytest.fail("numpy not imported under correct alias")


# Test image outputs using pytest-mpl
@pytest.mark.mpl_image_compare
def test_plot_derivative_approximations():
    return task_3.plot_derivative_approximations(
        func,
        true_derivative,
        [-2, 2],
        [1, 0.5, 0.1, 0.01],
    )
