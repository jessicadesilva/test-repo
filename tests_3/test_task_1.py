import pytest

from homework import task_1

def test_is_even():
    assert task_1.is_even(2) == True, f"Expected is_even(2) to be True, but got {task_1.is_even(2)}"
    assert task_1.is_even(3) == False, f"Expected is_even(3) to be False, but got {task_1.is_even(3)}"
    assert task_1.is_even(0) == True, f"Expected is_even(0) to be True, but got {task_1.is_even(0)}"
    assert task_1.is_even(-4) == True, f"Expected is_even(-4) to be True, but got {task_1.is_even(-4)}"

def test_max_of_two():
    assert task_1.max_of_two(1, 2) == 2, f"Expected max_of_two(1, 2) to be 2, but got {task_1.max_of_two(1, 2)}"
    assert task_1.max_of_two(5, 3) == 5, f"Expected max_of_two(5, 3) to be 5, but got {task_1.max_of_two(5, 3)}"
    assert task_1.max_of_two(-1, -2) == -1, f"Expected max_of_two(-1, -2) to be -1, but got {task_1.max_of_two(-1, -2)}"
    assert task_1.max_of_two(0, 0) == 0, f"Expected max_of_two(0, 0) to be 0, but got {task_1.max_of_two(0, 0)}"

def test_is_vowel():
    assert task_1.is_vowel('a') == True, f"Expected is_vowel('a') to be True, but got {task_1.is_vowel('a')}"
    assert task_1.is_vowel('e') == True, f"Expected is_vowel('e') to be True, but got {task_1.is_vowel('e')}"
    assert task_1.is_vowel('i') == True, f"Expected is_vowel('i') to be True, but got {task_1.is_vowel('i')}"
    assert task_1.is_vowel('o') == True, f"Expected is_vowel('o') to be True, but got {task_1.is_vowel('o')}"
    assert task_1.is_vowel('u') == True, f"Expected is_vowel('u') to be True, but got {task_1.is_vowel('u')}"
    assert task_1.is_vowel('b') == False, f"Expected is_vowel('b') to be False, but got {task_1.is_vowel('b')}"
    assert task_1.is_vowel('z') == False, f"Expected is_vowel('z') to be False, but got {task_1.is_vowel('z')}"
    assert task_1.is_vowel('z') == False, f"Expected is_vowel('z') to be False, but got {task_1.is_vowel('Z')}"
    assert task_1.is_vowel('A') == True, f"Expected is_vowel('A') to be True, but got {task_1.is_vowel('A')}"
    assert task_1.is_vowel('E') == True, f"Expected is_vowel('E') to be True, but got {task_1.is_vowel('E')}"
    assert task_1.is_vowel('I') == True, f"Expected is_vowel('I') to be True, but got {task_1.is_vowel('I')}"
    assert task_1.is_vowel('O') == True, f"Expected is_vowel('O') to be True, but got {task_1.is_vowel('O')}"
    assert task_1.is_vowel('U') == True, f"Expected is_vowel('U') to be True, but got {task_1.is_vowel('U')}"


def test_sign_of_number():
    assert task_1.sign_of_number(10) == "Positive", f"Expected sign_of_number(10) to be 'Positive', but got {task_1.sign_of_number(10)}"
    assert task_1.sign_of_number(-5) == "Negative", f"Expected sign_of_number(-5) to be 'Negative', but got {task_1.sign_of_number(-5)}"
    assert task_1.sign_of_number(0) == "Zero", f"Expected sign_of_number(0) to be 'Zero', but got {task_1.sign_of_number(0)}"
    assert task_1.sign_of_number(-0.5) == "Negative", f"Expected sign_of_number(-0.5) to be 'Negative', but got {task_1.sign_of_number(-0.5)}"
    assert task_1.sign_of_number(0.1) == "Positive", f"Expected sign_of_number(0.1) to be 'Positive', but got {task_1.sign_of_number(0.1)}"

if __name__ == "__main__":
    test_is_even()
    test_max_of_two()
    test_is_vowel()
    test_sign_of_number()
