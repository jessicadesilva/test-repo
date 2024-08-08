import pytest
from unittest.mock import patch, call
from task_2

def test_module_import():
  try:
    task_2.task_1.calculate_absolute_error(0, 0)
  except AttributeError:
    pytest.fail("task_1 module was not imported")

@pytest.mark.parametrize(
    "input, expected",
    (
        (-2, -219),
        (-1, 3),
        (0, 1),
        (1, 5),
        (2, 289),
        (3, 2265),
    ),
)
def test_example_function(input: float, expected: float) -> None:
    assert (
        task_2.example_function(input) == expected
    ), f"\n\nInput: example_function({input})\nExpected output: {expected}\n\n"

@pytest.mark.parametrize(
    "input, expected",
    (
        (-2, -776),
        (-1, -82),
        (0, 0),
        (1, 82),
    ),
)
def test_true_second_derivative(input: float, expected: float) -> None:
  assert (
        task_2.true_second_derivative(input) == expected
    ), f"\n\nInput: true_second_derivative({input})\nExpected output: {expected}\n\n"

def test_variable_definitions():
  assert task_2.x_value == 4, "\n\nInput: x_value\nExpected output: 4\n\n"
  assert task_2.h_values == [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625],
  "\n\nInput: h_values\nExpected output: [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625]\n\n"

@patch('task_1.plot_second_derivative_approximation')
def test_plot_second_derivative_approximation(mock_plot):
    # Call the function with the expected parameters
    x_value = 4
    h_values = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625]
    task_1.plot_second_derivative_approximation(task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Define the expected arguments
    expected_args = (task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Check if the mock function was called with the expected arguments
    mock_plot.assert_called_once_with(*expected_args)

@patch('task_1.plot_absolute_difference')
def test_plot_absolute_difference(mock_plot):
    # Call the function with the expected parameters
    x_value = 4
    h_values = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625]
    task_1.plot_absolute_difference(task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Define the expected arguments
    expected_args = (task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Check if the mock function was called with the expected arguments
    mock_plot.assert_called_once_with(*expected_args)
