import pytest
from unittest.mock import patch, call
from task_2

def test_module_import():
  try:
    task_2.task_1.calculate_absolute_error(0, 0)
  except AttributeError:
    pytest.fail("task_1 module was not imported")

def test_example_function():
    assert task_2.example_function(-2) == -219, f"Expected example_function(-2) = -219, but got {task_2.example_function(-2)}"
    assert task_2.example_function(-1) == 3, f"Expected example_function(-1) = 3, but got {task_2.example_function(-1)}"
    assert task_2.example_function(-0) == 1, f"Expected example_function(0) = 1, but got {task_2.example_function(0)}"
    assert task_2.example_function(1) == 5, f"Expected example_function(1) = 5, but got {task_2.example_function(1)}"
    assert task_2.example_function(2) == 289, f"Expected example_function(2) = 289, but got {task_2.example_function(2)}"
    assert task_2.example_function(3) == 2265, f"Expected example_function(3) = 2265, but got {task_2.example_function(3)}"

def test_true_second_derivative():
  assert task_2.true_second_derivative(-2) == -776, f"Expected true_second_derivative(-1) = -776, but got {task_2.true_second_derivative(-2)}"
  assert task_2.true_second_derivative(-1) == -82, f"Expected true_second_derivative(-1) = -82, but got {task_2.true_second_derivative(-1)}"
  assert task_2.true_second_derivative(0) == 0, f"Expected true_second_derivative(0) = 0, but got {task_2.true_second_derivative(0)}"
  assert task_2.true_second_derivative(1) == 82, f"Expected true_second_derivative(1) = 82, but got {task_2.true_second_derivative(1)}"

@patch('task_1.plot_second_derivative_approximation')
def test_plot_second_derivative_approximation(mock_plot):
    # Call the function with the expected parameters
    x_value = 4
    h_values = [2**(-x) for x in range(11)]
    task_1.plot_second_derivative_approximation(task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Define the expected arguments
    expected_args = (task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Check if the mock function was called with the expected arguments
    mock_plot.assert_called_once_with(*expected_args)

@patch('task_1.plot_absolute_difference')
def test_plot_absolute_difference(mock_plot):
    # Call the function with the expected parameters
    x_value = 4
    h_values = [2**(-x) for x in range(11)]
    task_1.plot_absolute_difference(task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Define the expected arguments
    expected_args = (task_2.example_function, task_2.true_second_derivative, x_value, h_values)

    # Check if the mock function was called with the expected arguments
    mock_plot.assert_called_once_with(*expected_args)
