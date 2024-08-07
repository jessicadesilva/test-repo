from homework import task_2

def test_product_list():
    assert task_2.product_list([1, 2, 3, 4]) == 24, f"Expected product_list([1, 2, 3, 4]) to be 24, but got {task_2.product_list([1, 2, 3, 4])}"
    assert task_2.product_list([2, 3, 5]) == 30, f"Expected product_list([2, 3, 5]) to be 30, but got {task_2.product_list([2, 3, 5])}"
    assert task_2.product_list([10]) == 10, f"Expected product_list([10]) to be 10, but got {task_2.product_list([10])}"
    assert task_2.product_list([1, 1, 1]) == 1, f"Expected product_list([1, 1, 1]) to be 1, but got {task_2.product_list([1, 1, 1])}"

def test_sum_of_squares():
    assert task_2.sum_of_squares(3) == 14, f"Expected sum_of_squares(3) to be 14, but got {task_2.sum_of_squares(3)}"
    assert task_2.sum_of_squares(5) == 55, f"Expected sum_of_squares(5) to be 55, but got {task_2.sum_of_squares(5)}"
    assert task_2.sum_of_squares(1) == 1, f"Expected sum_of_squares(1) to be 1, but got {task_2.sum_of_squares(1)}"
    assert task_2.sum_of_squares(0) == 0, f"Expected sum_of_squares(0) to be 0, but got {task_2.sum_of_squares(0)}"

def test_factorial():
    assert task_2.factorial(3) == 6, f"Expected factorial(3) to be 6, but got {task_2.factorial(3)}"
    assert task_2.factorial(5) == 120, f"Expected factorial(5) to be 120, but got {task_2.factorial(5)}"
    assert task_2.factorial(1) == 1, f"Expected factorial(1) to be 1, but got {task_2.factorial(1)}"

def test_arithmetic_series():
    assert task_2.arithmetic_series(1, 1, 5) == 15, f"Expected arithmetic_series(1, 1, 5) to be 15, but got {task_2.arithmetic_series(1, 1, 5)}"
    assert task_2.arithmetic_series(2, 2, 3) == 12, f"Expected arithmetic_series(2, 2, 3) to be 12, but got {task_2.arithmetic_series(2, 2, 3)}"
    assert task_2.arithmetic_series(1, 0, 4) == 4, f"Expected arithmetic_series(1, 0, 4) to be 4, but got {task_2.arithmetic_series(1, 0, 4)}"
    assert task_2.arithmetic_series(3, -1, 3) == 6, f"Expected arithmetic_series(3, -1, 3) to be 6, but got {task_2.arithmetic_series(3, -1, 3)}"

def test_geometric_series():
    assert task_2.geometric_series(1, 2, 3) == 7, f"Expected geometric_series(1, 2, 3) to be 7, but got {task_2.geometric_series(1, 2, 3)}"
    assert task_2.geometric_series(2, 3, 2) == 8, f"Expected geometric_series(2, 3, 2) to be 8, but got {task_2.geometric_series(2, 3, 2)}"
    assert task_2.geometric_series(1, 1, 4) == 4, f"Expected geometric_series(1, 1, 4) to be 4, but got {task_2.geometric_series(1, 1, 4)}"
    assert task_2.geometric_series(3, 0, 3) == 3, f"Expected geometric_series(3, 0, 3) to be 3, but got {task_2.geometric_series(3, 0, 3)}"
