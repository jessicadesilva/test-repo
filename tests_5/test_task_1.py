import pytest
from task_1 import newtons_method


# Define some test functions and their derivatives
def f1(x):
    return x**2 - 4


def f1_prime(x):
    return 2 * x


def f2(x):
    return x**3 - x - 2


def f2_prime(x):
    return 3 * x**2 - 1


def f3(x):
    return x**3


def f3_prime(x):
    return 3 * x**2


# Parameterized test cases for newtons_method
@pytest.mark.parametrize(
    "f, f_prime, x0, tol, max_iterations, expected_root",
    [
        (f1, f1_prime, 1.0, 1e-6, 100, 2.0),
        (f1, f1_prime, -1.0, 1e-6, 100, -2.0),
        (f2, f2_prime, 1.5, 1e-6, 100, 1.5213797),
        (f3, f3_prime, 0.1, 1e-6, 100, 0.0),
    ],
)
def test_newtons_method(f, f_prime, x0, tol, max_iterations, expected_root):
    # Run the Newton's method function
    root = newtons_method(f, f_prime, x0, tol, max_iterations)

    # Assert that the root found is within the tolerance level of the expected root
    assert pytest.approx(root) == expected_root

