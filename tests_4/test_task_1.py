import pytest
import task_1

# Define a test function and its true second derivative
def func(x):
    return x**3

def true_second_derivative(x):
    return 6*x

def test_central_difference_second_derivative():
    assert task_1.central_difference_second_derivative(func, 0, 0.01) == 0.0001, f"Expected {true_value} with f(x)=x^3, x=0, h=0.01, but got {estimated}"

def test_calculate_absolute_error():
    assert task_1.calculate_absolute_error(0.5, 0.45) == 0.05, f"Expected calculate_absolute_error(0.5, 0.45) = 0.05 but got {task_1.calculate_absolute_error(0.5, 0.45)}"
    assert task_1.calculate_absolute_error(0.45, 0.5) == 0.05, f"Expected calculate_absolute_error(0.45, 0.5) = 0.05 but got {task_1.calculate_absolute_error(0.45, 0.5)}"
    assert task_1.calculate_absolute_error(0.5, 0.5) == 0, f"Expected calculate_absolute_error(0.5, 0.5) = 0 but got {task_1.calculate_absolute_error(0.5, 0.5)}"

def test_package_import():
  try:
    task_1.plt.rcdefaults()
  except AttributeError:
    pytest.fail("matplotlib.pyplot was not imported as plt")

# Test image outputs using pytest-mpl
@pytest.mark.mpl_image_compare
def test_plot_second_derivative_approximation(mpl_image_path):
    # Define the parameters
    x_value = 0
    h_values = [1, 0.1, 0.01]
    
    # Generate the plot and save it to a file
    task_1.plot_second_derivative_approximation(func, true_second_derivative, x_value, h_values, filename='test_plot_second_derivative_approx.png')
    
    # The image is saved and will be compared to a reference image
    return 'test_plot_second_derivative_approx.png'

# Test image outputs using pytest-mpl
@pytest.mark.mpl_image_compare
def test_plot_absolute_errror(mpl_image_path):
    # Define the parameters
    x_value = 0
    h_values = [1, 0.1, 0.01]
    
    # Generate the plot and save it to a file
    task_1.plot_absolute_error(func, true_second_derivative, x_value, h_values, filename='test_plot_absolute_error.png')
    
    # The image is saved and will be compared to a reference image
    return 'test_plot_absolute_error.png'
