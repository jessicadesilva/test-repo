import subprocess
import task_2


def test_list_computations():
    # Import variables from the task script
    numbers = task_2.numbers
    sum_numbers = task_2.sum_numbers
    average_numbers = task_2.average_numbers
    max_number = task_2.max_number
    min_number = task_2.min_number

    # Check the values
    expected_sum_numbers = sum(numbers)
    expected_average_numbers = expected_sum_numbers / len(numbers)
    expected_max_number = max(numbers)
    expected_min_number = min(numbers)

    assert (
        sum_numbers == expected_sum_numbers
    ), f"Expected sum_numbers to be {expected_sum_numbers} but got {sum_numbers}"
    assert (
        average_numbers == expected_average_numbers
    ), f"Expected average_numbers to be {expected_average_numbers} but got {average_numbers}"
    assert (
        max_number == expected_max_number
    ), f"Expected max_number to be {expected_max_number} but got {max_number}"
    assert (
        min_number == expected_min_number
    ), f"Expected min_number to be {expected_min_number} but got {min_number}"


def test_printed_output():
    # Run the task script
    result = subprocess.run(
        ["python", "./homework/task_2.py"], capture_output=True, text=True
    )

    sum_numbers = task_2.sum_numbers
    average_numbers = task_2.average_numbers
    max_number = task_2.max_number
    min_number = task_2.min_number

    # Check the printed output
    expected_output = (
        f"Sum of all numbers: {sum_numbers}\n"
        f"Average of numbers: {average_numbers}\n"
        f"Maximum number: {max_number}\n"
        f"Minimum number: {min_number}\n"
    )
    assert (
        result.stdout == expected_output
    ), f"Expected '{expected_output}' but got '{result.stdout}'"


if __name__ == "__main__":
    test_list_computations()
    test_printed_output()
