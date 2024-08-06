import subprocess
import sys
import os

# Add the parent directory to sys.path to enable import of task_2
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import task_2

def test_average_value():
    assert task_2.average_value(2, 4) == 3, f"Expected average_value(2, 4) to be 3, but got {task_2.average_value(2, 4)}"
    assert task_2.average_value(0, 0) == 0, f"Expected average_value(0, 0) to be 0, but got {task_2.average_value(0, 0)}"
    assert task_2.average_value(-2, 2) == 0, f"Expected average_value(-2, 2) to be 0, but got {task_2.average_value(-2, 2)}"
    assert task_2.average_value(1.5, -1.5) == 0, f"Expected average_value(1, -1) to be 0, but got {task_2.average_value(1, -1)}"

def test_max_of_three():
    assert task_2.max_of_three(1, 2, 3) == 3, f"Expected max_of_three(1, 2, 3) to be 3, but got {task_2.max_of_three(1, 2, 3)}"
    assert task_2.max_of_three(3, 2, 1) == 3, f"Expected max_of_three(3, 2, 1) to be 3, but got {task_2.max_of_three(3, 2, 1)}"
    assert task_2.max_of_three(-1, -2, -3) == -1, f"Expected max_of_three(-1, -2, -3) to be -1, but got {task_2.max_of_three(-1, -2, -3)}"
    assert task_2.max_of_three(0, 0, 0) == 0, f"Expected max_of_three(0, 0, 0) to be 0, but got {task_2.max_of_three(0, 0, 0)}"

def test_min_of_three():
    assert task_2.min_of_three(1, 2, 3) == 1, f"Expected min_of_three(1, 2, 3) to be 1, but got {task_2.min_of_three(1, 2, 3)}"
    assert task_2.min_of_three(3, 2, 1) == 1, f"Expected min_of_three(3, 2, 1) to be 1, but got {task_2.min_of_three(3, 2, 1)}"
    assert task_2.min_of_three(-1, -2, -3) == -3, f"Expected min_of_three(-1, -2, -3) to be -3, but got {task_2.min_of_three(-1, -2, -3)}"
    assert task_2.min_of_three(0, 0, 0) == 0, f"Expected min_of_three(0, 0, 0) to be 0, but got {task_2.min_of_three(0, 0, 0)}"

def test_midrange():
    assert task_2.midrange(1, 2, 3) == 2, f"Expected midrange(1, 2, 3) to be 2, but got {task_2.midrange(1, 2, 3)}"
    assert task_2.midrange(3, 2, 1) == 2, f"Expected midrange(3, 2, 1) to be 2, but got {task_2.midrange(3, 2, 1)}"
    assert task_2.midrange(-1, -2, -3) == -2, f"Expected midrange(-1, -2, -3) to be -2, but got {task_2.midrange(-1, -2, -3)}"
    assert task_2.midrange(0, 0, 0) == 0, f"Expected midrange(0, 0, 0) to be 0, but got {task_2.midrange(0, 0, 0)}"

if __name__ == "__main__":
    test_average_value()
    test_max_of_three()
    test_min_of_three()
    test_midrange()
