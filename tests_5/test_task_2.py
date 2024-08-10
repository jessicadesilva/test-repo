import pytest
import task_2


def f1(x):
    return x**2


def f2(x):
    return x**3 - 3 * x + 2


@pytest.mark.parametrize(
    "x, expected_derivative",
    [
        (1.0, 2.0),
        (-1.0, -2.0),
    ],
)
def test_central_difference_f1(x, expected_derivative):
    # Calculate the approximate derivative
    approx_derivative = task_2.central_difference(f1, x)

    # Assert that the approximate derivative is close to the expected derivative
    assert (
        approx_derivative == pytest.approx(expected_derivative, abs=1e-4)
    ), f"\n\nInput: central_difference(x^2, {x})\nExpected output: {expected_derivative}\n\n"


@pytest.mark.parametrize(
    "x, expected_derivative",
    [
        (1.0, 0.0),
        (2.0, 9.0),
    ],
)
def test_central_difference_f2(x, expected_derivative):
    # Calculate the approximate derivative
    approx_derivative = task_2.central_difference(f2, x)

    # Assert that the approximate derivative is close to the expected derivative
    assert (
        approx_derivative == pytest.approx(expected_derivative, abs=1e-4)
    ), f"\n\nInput: central_difference(x^3-3x+2, {x})\nExpected output: {expected_derivative}\n\n"


def test_import_plt():
    try:
        task_2.plt.rcdefaults()
    except AttributeError:
        pytest.fail("matplotlib.pyplot not imported")


def test_import_np():
    try:
        task_2.np.pi
    except AttributeError:
        pytest.fail("numpy not imported")


def test_import_newtons():
    try:
        task_2.newtons_method
    except AttributeError:
        pytest.fail("newtons_method not imported from task_1")

@pytest.mark.mpl_image_compare
def test_plot_newtons_method():
    return task_2.plot_newtons_method(f2, (0, 2))
