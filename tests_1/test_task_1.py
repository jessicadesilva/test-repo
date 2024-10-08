import task_1
import subprocess

def test_exponentiation_result():
    # Import variables from the task script
    a = task_1.a
    b = task_1.b
    result = task_1.result

    # Check the result
    expected_result = a**b

    assert (
        result == expected_result
    ), f"Expected result to be {expected_result} but got {result}"


def test_printed_output():
    # Import result variable from the task script
    result = task_1.result

    # Run the task script
    console_out = subprocess.run(
        ["python", "task_1.py"], capture_output=True, text=True
    )

    # Check the printed output
    expected_output = (
        f"Result: {result}\n"  # Adjust based on example values in the task script
    )
    assert (
        console_out.stdout == expected_output
    ), f"Expected '{expected_output}' but got '{console_out.stdout}'"
