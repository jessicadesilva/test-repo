import pytest

# Parameterized tests for the function f(x)
@pytest.mark.parametrize("input_value, expected_output", [
    (0, 2),  # Test case 1: f(0) should return 2
    (1, 3),  # Test case 2: f(1) should return 3
    (-1, 1), # Test case 3: f(-1) should return 1
    (5, 7),  # Test case 4: f(5) should return 7
    (10, 12) # Test case 5: f(10) should return 12
])
def test_f(input_value, expected_output):
    assert f(input_value) == expected_output, f"\n\nInput: f({input_value})\nExpected output: {expected_output}\n\n"
