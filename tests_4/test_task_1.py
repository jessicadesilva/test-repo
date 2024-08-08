import pytest
import task_1


# Define a test function and its true second derivative
def func(x):
    return 3 * x**4 - 5 * x**3 + 2 * x**2 - 7 * x + 6


def true_second_derivative(x):
    return 36 * x**2 - 30 * x + 4


def test_central_difference_second_derivative():
    assert (
        task_1.central_difference_second_derivative(func, 3, 1) == pytest.approx(244)
    ), "\n\nInput: central_difference_second_derivative(f, 3, 1) with f(x) = 3x^4-5x^3+2x^2-7x+6\nExpected output: Approximately 244\n\n"


@pytest.mark.parametrize(
    "est, true, expected",
    (
        (0.5, 0.45, 0.05),
        (0.45, 0.5, 0.05),
        (0.5, 0.5, 0),
    ),
)
def test_calculate_absolute_error(est: float, true: float, expected: float) -> None:
    assert (
        task_1.calculate_absolute_error(est, true) == pytest.approx(expected)
    ), f"\n\nInput: task_1.calculate_absolute_error({est}, {true})\nExpected output: {expected}\n\n"


def test_package_import():
    try:
        task_1.plt.rcdefaults()
    except AttributeError:
        pytest.fail("matplotlib.pyplot was not imported as plt")


# Test image outputs using pytest-mpl
@pytest.mark.mpl_image_compare
def test_plot_second_derivative_approximation():
    # Define the parameters
    x_value = 3
    h_values = [1, 0.5, 0.1, 0.01]

    return task_1.plot_second_derivative_approximation(
        func, true_second_derivative, x_value, h_values
    )


# Test image outputs using pytest-mpl
@pytest.mark.mpl_image_compare
def test_plot_absolute_error():
    # Define the parameters
    x_value = 3
    h_values = [1, 0.5, 0.1, 0.01]

    return task_1.plot_absolute_error(
        func,
        true_second_derivative,
        x_value,
        h_values,
    )
