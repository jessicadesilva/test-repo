import subprocess
import sys
import os

# Add the parent directory to sys.path to enable import of task_1
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import task_1

def test_linear_function():
    assert task_1.linear_function(0) == 3, f"Expected linear_function(0) to be 3, but got {task_1.linear_function(0)}"
    assert task_1.linear_function(1) == 5, f"Expected linear_function(1) to be 5, but got {task_1.linear_function(1)}"
    assert task_1.linear_function(-1) == 1, f"Expected linear_function(-1) to be 1, but got {task_1.linear_function(-1)}"
    assert task_1.linear_function(2) == 7, f"Expected linear_function(7) to be 7, but got {task_1.linear_function(7)}"

def test_constant_function():
    assert task_1.constant_function(0) == 4, "Expected constant_function(0) to be 4, but got {task_1.constant_function(0)}"
    assert task_1.constant_function(10) == 4, "Expected constant_function(10) to be 4, but got {task_1.constant_function(10)}"
    assert task_1.constant_function(-5) == 4, "Expected constant_function(-5) to be 4, but got {task_1.constant_function(-5)}"
    assert task_1.constant_function(0.5) == 4, "Expected constant_function(0.5) to be 4, but got {task_1.constant_function(0.5)}"

def test_exponential_function():
    assert task_1.exponential_function(0) == 1, f"Expected exponential_function(0) to be 1, but got {task_1.exponential_function(0)}"
    assert task_1.exponential_function(1) == 2, f"Expected exponential_function(1) to be 2, but got {task_1.exponential_function(1)}"
    assert task_1.exponential_function(2) == 4, f"Expected exponential_function(2) to be 4, but got {task_1.exponential_function(2)}"
    assert task_1.exponential_function(-1) == 0.5, f"Expected exponential_function(-1) to be 0.5, but got {task_1.exponential_function(-1)}"

def test_absolute_value():
    assert task_1.absolute_value(0) == 0, "Expected absolute_value(0) to be 0, but got {task_1.absolute_value(0)}"
    assert task_1.absolute_value(1) == 1, "Expected absolute_value(1) to be 1, but got {task_1.absolute_value(1)}"
    assert task_1.absolute_value(-1) == 1, "Expected absolute_value(-1) to be 1, but got {task_1.absolute_value(-1)}"
    assert task_1.absolute_value(2.5) == 2.5, "Expected absolute_value(2.5) to be 2.5, but got {task_1.absolute_value(2.5)}"
    assert task_1.absolute_value(-2.5) == 2.5, "Expected absolute_value(-2.5) to be 2.5, but got {task_1.absolute_value(-2.5)}"

if __name__=="__main__":
    test_linear_function()
    test_constant_function()
    test_exponential_function()
    test_absolute_value()
