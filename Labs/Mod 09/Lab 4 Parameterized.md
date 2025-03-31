
# Lab 9-4: Parameterized Testing with Pytest



## Project Structure

Same as the previous labs

```
project/
├── app/
│   └── calc.py              # Code under test
└── tests/
    └── test_calc.py         # Your tests
```

---

## Problem 1: Testing the Same Function with Multiple Inputs

You want to test a simple function like `add(a, b)` with different inputs without repeating test code.

### olution: Use `@pytest.mark.parametrize`

### Code: `app/calc.py`

```python
def add(a, b):
    return a + b
```

### Code: `tests/test_calc.py`

```python
import pytest
from app.calc import add

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Explanation:
- The test runs 3 times, once for each input set
- `pytest` injects `a`, `b`, and `expected` into each test run

---

## Problem 2: Test Input Variations for a Validator Function

You want to test a function that checks if a string is a palindrome.

### Solution: Use Parametrized Booleans

### Add to `app/calc.py`

```python
def is_palindrome(s):
    return s == s[::-1]
```

### Add to `tests/test_calc.py`

```python
from app.calc import is_palindrome # Add at the top of  the file

@pytest.mark.parametrize("s,expected", [
    ("radar", True),
    ("hello", False),
    ("", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected
```
 
Run the code with `pytest -v` to see the results

---

## Problem 3: Use `ids` to Make Test Output More Readable

Your test cases are working, but the output is hard to understand.

### Solution: Add `ids` for custom test case labels

Add this code to the test file

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 2, 4),
    (10, 5, 15),
    (3, 0, 3)
], ids=["equal-nums", "positive-mix", "zero-add"])
def test_add_readable(a, b, expected):
    assert add(a, b) == expected
```


```bash
test_calc.py::test_add_readable[equal-nums] PASSED
test_calc.py::test_add_readable[positive-mix] PASSED
test_calc.py::test_add_readable[zero-add] PASSED
```

---

## Problem 4: Test One Input Against Many Expected Results

You want to test how your function handles a single pattern with many strings.

### Solution: Parameterize with one changing value
 
Add to the test file (you can delete the other tests)

```python
@pytest.mark.parametrize("s", ["radar", "madam", "step on no pets"])
def test_valid_palindromes(s):
    assert is_palindrome(s)
```
