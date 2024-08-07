import task_3


def test_console_output():
    # Run the task script
    result = subprocess.run(
        ["python", "./homework/task_3.py"], capture_output=True, text=True
    )

    # Check the printed output
    expected_output = (
        f"Hello, world!\n"
        f"The value of x is 5\n"
        f"The first number in the list numbers is 1\n"
        f"There are 3 numbers in the list called numbers.\n"
    )
    assert (
        result.stdout == expected_output
    ), f"Expected '{expected_output}' but got '{result.stdout}'"


def test_message_variable():
    message = task_3.message
    assert message == "Greetings", f"Expected Greetings but got {message}"
