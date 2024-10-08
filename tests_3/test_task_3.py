import pytest
import math

import task_3

def test_approximate_euler_number():
    tol = 1e-7
    expected_value = math.e
    approx_value = task_3.approximate_euler_number(tol)
    assert abs(approx_value - expected_value) < tol, f"Expected approximate_euler_number({tol}) to be close to {expected_value}, but got {approx_value}"

def test_approximate_ln():
    tol = 1e-7
    x_values = [0.6, 1.0, 1.5, 1.99]
    for x in x_values:
        expected_value = math.log(x)
        approx_value = task_3.approximate_ln(x, tol)
        assert abs(approx_value - expected_value) < tol, f"Expected approximate_ln({x}, {tol}) to be close to {expected_value}, but got {approx_value}"

def test_approximate_cos():
    tol = 1e-7
    x_values = [-math.pi, -math.pi / 2, 0, math.pi / 2, math.pi]
    for x in x_values:
        expected_value = math.cos(x)
        approx_value = task_3.approximate_cos(x, tol)
        assert abs(approx_value - expected_value) < tol, f"Expected approximate_cos({x}, {tol}) to be close to {expected_value}, but got {approx_value}"
