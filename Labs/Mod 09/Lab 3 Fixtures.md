
# Lab 9-3: Using Fixtures in Pytest

#

## Project Structure

```
9-3-Project/
├── app/
│   └── calc.py           # Code under test
└── tests/
    └── test_calc.py      # Your tests
```

---

## Part 1: Repeating Setup Code in Every Test

### Problem:

You are testing a calculator module that performs basic arithmetic operations. 

Different users may have different preferences when it comes to how results are displayed or whether detailed logging is shown. 

Your task is to:
- Write unit tests for the add() and subtract() functions.
- Use pytest fixtures to simulate users with different preferences.
- Ensure your tests check both the correctness of the results and that the preferences are being respected (e.g., rounding is applied when requested).

The user preferences include:
- verbose: whether to print calculation details (simulated with print())
- round_result: whether to round the result
- precision: how many decimal places to round to

Code to be tested:

```python

```

### Solution: Use a Basic Fixture

### Code: `app/calc.py`

```python
def add(a, b, verbose=False, round_result=False, precision=2):
    result = a + b
    if verbose:
        print(f"Adding {a} and {b}, result = {result}")
    if round_result:
        result = round(result, precision)
    return result

def subtract(a, b, verbose=False, round_result=False, precision=2):
    result = a - b
    if verbose:
        print(f"Subtracting {b} from {a}, result = {result}")
    if round_result:
        result = round(result, precision)
    return result

```

### Code: `tests/test_calc.py`

These fixtures return dictionaries that represent user preferences. 
- They’re injected into the tests that follow.

```python

import pytest
from app.calc import add, subtract

# Fixture: user with verbose output and no rounding
@pytest.fixture
def verbose_user():
    return {
        "username": "alice",
        "verbose": True,
        "round_result": False,
        "precision": 2
    }

# Fixture: user who wants results rounded to 1 decimal place
@pytest.fixture
def rounding_user():
    return {
        "username": "bob",
        "verbose": False,
        "round_result": True,
        "precision": 1
    }

def test_add_verbose(verbose_user):
    result = add(2.345, 3.111,
                 verbose=verbose_user["verbose"],
                 round_result=verbose_user["round_result"],
                 precision=verbose_user["precision"])
    assert result == 5.456  # no rounding applied

def test_subtract_rounded(rounding_user):
    result = subtract(5.55, 2.123,
                      verbose=rounding_user["verbose"],
                      round_result=rounding_user["round_result"],
                      precision=rounding_user["precision"])
    assert result == 3.4  # rounded to 1 decimal

def test_add_rounding_precision_2():
    # Direct test without using a fixture
    result = add(1.235, 2.346, round_result=True, precision=2)
    assert result == 3.58

```

---

## Problem 2: You Need Setup and Teardown Logic

### Problem:
You want to simulate opening and closing a resource (like a file or connection).

### Solution: Use `yield` in a Fixture

### Code: replace the code in `tests/test_calc.py` with this code

```python

import pytest 

@pytest.fixture
def open_resource():
    print("Setup: Opening resource")
    yield "resource_object"
    print("Teardown: Closing resource")

def test_resource_usage(open_resource):
    assert open_resource == "resource_object"
```

### Explanation:
- Code **before `yield`** runs before the test (setup)
- Code **after `yield`** runs after the test (teardown)
- This simulates managing resources like files, DBs, or network calls

Run with:

```bash
pytest -s
```

And you’ll see:

```
Setup: Opening resource
Teardown: Closing resource
```

---

## Problem 3: You Want to Use Multiple Fixtures Together

### Problem:
You want to combine user setup and resource setup in the same test.

### Solution: Pass Multiple Fixtures

```python
import pytest

# Fixture 1: Simulated user object
@pytest.fixture
def test_user():
    print("\n[SETUP] Creating test user...")
    user = {
        "username": "testuser",
        "role": "admin"
    }
    yield user
    print("[TEARDOWN] Cleaning up test user...")

# Fixture 2: Simulated resource (e.g., DB connection or file)
@pytest.fixture
def open_resource():
    print("[SETUP] Opening resource...")
    resource = "resource_object"
    yield resource
    print("[TEARDOWN] Closing resource...")

# Test using both fixtures
def test_combined_use(test_user, open_resource):
    print("[TEST] Running test_combined_use...")

```

### Explanation:
- `pytest` resolves **both fixtures** and injects them in order
- Setup runs in **left-to-right order**
- Teardown runs in **reverse order**
