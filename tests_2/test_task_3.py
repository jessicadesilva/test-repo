import subprocess
import sys
import os

# Add the parent directory to sys.path to enable import of task_3
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import task_3

def test_first_element():
    assert task_3.first_element([1, 2, 3]) == 1, f"Expected first_element([1, 2, 3]) to be 1, but got {task_3.first_element([1, 2, 3])}"
    assert task_3.first_element([1]) == 1, f"Expected first_element([1]) to be 1, but got {task_3.first_element([1])}"
    assert task_3.first_element(['a', 'b', 'c']) == 'a', f"Expected first_element(['a', 'b', 'c']) to be 'a', but got {task_3.first_element(['a', 'b', 'c'])}"
    assert task_3.first_element([True, False]) == True, f"Expected first_element([True, False]) to be True, but got {task_3.first_element([True, False])}"

def test_last_element():
    assert task_3.last_element([1, 2, 3]) == 3, f"Expected last_element([1, 2, 3]) to be 3, but got {task_3.last_element([1, 2, 3])}"
    assert task_3.last_element([1]) == 1, f"Expected last_element([1]) to be 1, but got {task_3.last_element([1])}"
    assert task_3.last_element(['a', 'b', 'c']) == 'c', f"Expected last_element(['a', 'b', 'c']) to be 'c', but got {task_3.last_element(['a', 'b', 'c'])}"
    assert task_3.last_element([True, False]) == False, f"Expected last_element([True, False]) to be False, but got {task_3.last_element([True, False])}"

def test_first_last_sum():
    assert task_3.first_last_sum([1, 2, 3]) == 4, f"Expected first_last_sum([1, 2, 3]) to be 4, but got {task_3.first_last_sum([1, 2, 3])}"
    assert task_3.first_last_sum([1]) == 2, f"Expected first_last_sum([1]) to be 2, but got {task_3.first_last_sum([1])}"
    assert task_3.first_last_sum([4, 3, 2, -1]) == 3, f"Expected first_last_sum([4, 3, 2, -1]) to be 3, but got {task_3.first_last_sum([4, 3, 2, -1])}"

def test_distance_from_origin():
    assert task_3.distance_from_origin((3, 4)) == 5, f"Expected distance_from_origin((3, 4)) to be 5, but got {task_3.distance_from_origin((3, 4))}"
    assert task_3.distance_from_origin((0, 0)) == 0, f"Expected distance_from_origin((0, 0)) to be 0, but got {task_3.distance_from_origin((0, 0))}"
    assert task_3.distance_from_origin((-3, -4)) == 5, f"Expected distance_from_origin((-3, -4)) to be 5, but got {task_3.distance_from_origin((-3, -4))}"

def test_distance_between():
    assert task_3.distance_between((1, 2), (4, 6)) == 5, f"Expected distance_between((1, 2), (4, 6)) to be 5, but got {task_3.distance_between((1, 2), (4, 6))}"
    assert task_3.distance_between((0, 0), (0, 0)) == 0, f"Expected distance_between((0, 0), (0, 0)) to be 0, but got {task_3.distance_between((0, 0), (0, 0))}"
    assert task_3.distance_between((-1, -1), (-4, -5)) == 5, f"Expected distance_between((-1, -1), (-4, -5)) to be 5, but got {task_3.distance_between((-1, -1), (-4, -5))}"

if __name__ == "__main__":
    test_first_element()
    test_last_element()
    test_first_last_sum()
    test_distance_from_origin()
    test_distance_between()
