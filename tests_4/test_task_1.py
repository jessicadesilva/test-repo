import pytest
from homework import task_1


# Define a test function and its true second derivative
def func(x):
    return x**3


def true_second_derivative(x):
    return 6 * x


def test_central_difference_second_derivative():
    assert (
        task_1.central_difference_second_derivative(func, 0, 0.01) == 0
    )  # , f"Expected 0 with f(x)=x^3, x=0, h=0.01, but got {task_1.central_difference_second_derivative(func, 0, 0.01)}"


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
    # , f"Expected calculate_absolute_error({est}, {true}) = {expected} but got {task_1.calculate_absolute_error(est, true)}"


def test_package_import():
    try:
        task_1.plt.rcdefaults()
    except AttributeError:
        pytest.fail("matplotlib.pyplot was not imported as plt")


# Test image outputs using pytest-mpl
@pytest.mark.mpl_image_compare
def test_plot_second_derivative_approximation():
    # Define the parameters
    x_value = 5
    h_values = [1, 0.1, 0.01]

    # Generate the plot and save it to a file
    return task_1.plot_second_derivative_approximation(
        func, true_second_derivative, x_value, h_values
    )


# Test image outputs using pytest-mpl
@pytest.mark.mpl_image_compare
def test_plot_absolute_error():
    # Define the parameters
    x_value = 5
    h_values = [1, 0.1, 0.01]

    # Generate the plot and save it to a file
    return task_1.plot_absolute_error(
        func,
        true_second_derivative,
        x_value,
        h_values,
    )
