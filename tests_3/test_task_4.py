import task_4  # Make sure the task_4 module is imported

def test_is_prime():
    assert task_4.is_prime(-2) == False, "Expected is_prime(-2) to be False"
    assert task_4.is_prime(0) == False, "Expected is_prime(0) to be False"
    assert task_4.is_prime(1) == False, "Expected is_prime(1) to be False"
    assert task_4.is_prime(2) == True, "Expected is_prime(2) to be True"
    assert task_4.is_prime(3) == True, "Expected is_prime(3) to be True"
    assert task_4.is_prime(4) == False, "Expected is_prime(4) to be False"
    assert task_4.is_prime(5) == True, "Expected is_prime(5) to be True"
    assert task_4.is_prime(10) == False, "Expected is_prime(10) to be False"

def test_fibonacci():
    assert task_4.fibonacci(1) == 0, f"Expected fibonacci(1) to be 0, but got {task_4.fibonacci(1)}"
    assert task_4.fibonacci(2) == 1, f"Expected fibonacci(2) to be 1, but got {task_4.fibonacci(2)}"
    assert task_4.fibonacci(3) == 1, f"Expected fibonacci(3) to be 1, but got {task_4.fibonacci(3)}"
    assert task_4.fibonacci(4) == 2, f"Expected fibonacci(4) to be 2, but got {task_4.fibonacci(4)}"
    assert task_4.fibonacci(5) == 3, f"Expected fibonacci(5) to be 3, but got {task_4.fibonacci(5)}"
    assert task_4.fibonacci(6) == 5, f"Expected fibonacci(6) to be 5, but got {task_4.fibonacci(6)}"
    assert task_4.fibonacci(10) == 34, f"Expected fibonacci(10) to be 34, but got {task_4.fibonacci(10)}"

def test_prime_fibonacci():
    assert task_4.prime_fibonacci(1) == [2], f"Expected prime_fibonacci(1) to be [2], but got {task_4.prime_fibonacci(1)}"
    assert task_4.prime_fibonacci(2) == [2, 3], f"Expected prime_fibonacci(2) to be [2, 3], but got {task_4.prime_fibonacci(2)}"
    assert task_4.prime_fibonacci(3) == [2, 3, 5], f"Expected prime_fibonacci(3) to be [2, 3, 5], but got {task_4.prime_fibonacci(3)}"
    assert task_4.prime_fibonacci(4) == [2, 3, 5, 13], f"Expected prime_fibonacci(4) to be [2, 3, 5, 13], but got {task_4.prime_fibonacci(4)}"
    assert task_4.prime_fibonacci(5) == [2, 3, 5, 13, 89], f"Expected prime_fibonacci(5) to be [2, 3, 5, 13, 89], but got {task_4.prime_fibonacci(5)}"
