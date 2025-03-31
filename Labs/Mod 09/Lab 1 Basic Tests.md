# Lab 9-1 Running Basic Tests with pytest

Ensure that you have installed pytest by running the code below in the same environment you will be running the lab in

```shell
pip install pytest
```

## Step 1 – Set Up Project Structure

Set up the following project structure on your machine. A copy of the files and directories is in the labs folder in the repository

```text
9-1-project/
├── app/                     ← Python code to be tested
│   ├── __init__.py
│   └── utils.py             ← Contains utility functions
│
└── tests/                   ← Test directory
    ├── __init__.py
    └── test_utils.py        ← Contains pytest test cases

```

Note that the __init__.py fles can be empty

## Step 2: Create the `utils.py` file 

Copy the following code into it

```python
# app/utils.py

def add(a, b):
    return a + b

def is_palindrome(s):
    return s == s[::-1]

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b

```
Each function has a clear purpose:
- add(a, b) → adds two numbers
- is_palindrome(s) → checks if a string is a palindrome
- divide(a, b) → divides two numbers, raises error on zero division

## Step 3: Create the tests/test_utils.py File

Copy the following code into it.

```python
# tests/test_utils.py

from app.utils import add, is_palindrome, divide
import pytest

# --- Tests for add() ---
def test_add_positive():
    assert add(3, 5) == 8

def test_add_negative():
    assert add(-4, -6) == -10

def test_add_zero():
    assert add(0, 10) == 10

# --- Tests for is_palindrome() ---
def test_palindrome_true():
    assert is_palindrome("radar") is True

def test_palindrome_false():
    assert is_palindrome("hello") is False

def test_palindrome_empty_string():
    assert is_palindrome("") is True

# --- Tests for divide() ---
def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-9, 3) == -3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

```

- We use pytest.raises() to test that an error is correctly raised
- There are multiple test cases per function

## Step 4: Run the tests

Open a terminal and navigate to the project/ root directory (where both app/ and tests/ exist).
- Use `conda activate labs` to ensure you are in the same environment where you have installed `pytest`

```shell
(base) 9-1-project$ conda activate labs
(labs) 9-1-project$ pytest
================================================================================== test session starts ===================================================================================
platform linux -- Python 3.12.9, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/rod/working/pytest/9-1-project
plugins: anyio-3.7.1
collected 9 items                                                                                                                                                                        

tests/test_utils.py .........                                                                                                                                                      [100%]

=================================================================================== 9 passed in 0.01s ====================================================================================
(labs) rod@exgnosis:~/working/pytest/9-1-project$ 

```

## Step 5: Introduce an error into the code

In the code for the `is_pallindrome()` simulate a programming error by making the following change

```python
def is_palindrome(s):
     # return s == s[::-1]
    return s == s[::1]
```

Rerun the tests.

```shell
9-1-project$ pytest
================================================================================== test session starts ===================================================================================
platform linux -- Python 3.12.9, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/rod/working/pytest/9-1-project
plugins: anyio-3.7.1
collected 9 items                                                                                                                                                                        

tests/test_utils.py ....F....                                                                                                                                                      [100%]

======================================================================================== FAILURES ========================================================================================
_________________________________________________________________________________ test_palindrome_false __________________________________________________________________________________

    def test_palindrome_false():
>       assert is_palindrome("hello") is False
E       AssertionError: assert True is False
E        +  where True = is_palindrome('hello')

tests/test_utils.py:21: AssertionError
================================================================================ short test summary info =================================================================================
FAILED tests/test_utils.py::test_palindrome_false - AssertionError: assert True is False
============================================================================== 1 failed, 8 passed in 0.04s ===============================================================================

```
Remove the error before moving on to the next section.

