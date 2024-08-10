import pytest
from task_1 import newtons_method


def f1(x):
    return x**2 - 4


def f1_prime(x):
    return 2 * x


def f2(x):
    return x**3 - x - 2


def f2_prime(x):
    return 3 * x**2 - 1


def f3(x):
    return x**3 - 3 * x + 2


def f3_prime(x):
    return 3 * x**2 - 3


# Parameterized test cases for newtons_method
@pytest.mark.parametrize(
    "x0, tol, max_iterations, expected_root",
    [
        (1.0, 1e-6, 100, 2.0),
        (-1.0, 1e-6, 100, -2.0),
    ],
)
def test_newtons_method_f1(x0, tol, max_iterations, expected_root):
    # Run the Newton's method function
    root = newtons_method(f1, f1_prime, x0, tol, max_iterations)

    # Assert that the root found is within the tolerance level of the expected root
    assert (
        root == pytest.approx(expected_root, abs=1e-5)
    ), f"\n\nInput: newtons_method(x^2-4, 2x, {x0}, {tol}, {max_iterations})\nExpected output: {expected_root}\n\n"


def test_newtons_method_f2():
    root = newtons_method(f2, f2_prime, 1.5, 1e-6, 100)
    assert (
        root == pytest.approx(1.5213797, abs=1e-5)
    ), "\n\nInput: newtons_method(x^3-x-2, 3x^2-1, 1.5, 1e-6, 100)\nExpected output: 1.5213797\n\n"


def test_newtons_method_f3():
    root = newtons_method(f3, f3_prime, 0.0, 1e-6, 10)
    assert (
        root == pytest.approx(0.9994243423847423, abs=1e-6)
    ), "\n\nInput: newtons_method(x^3-3x+2, 3x^2-3, 0, 1e-6, 10)\nExpected output: Maximum number of iterations reached. 0.9994243423847423\n\n"
