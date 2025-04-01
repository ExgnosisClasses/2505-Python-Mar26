# Lab 9-5: Test Classes


---

## Problem 1: Grouping Related Tests with a Test Class

You are testing a calculator module with `add()` and `subtract()` functions. You want to organize related tests into a class to improve readability and maintainability.

---

### Code: `app/calc.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

---

### Test Class Example: `tests/test_calc.py`

```python
from app.calc import add, subtract

class TestCalculator:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_with_zero(self):
        assert subtract(7, 0) == 7
```

---

### Run the Test Class

```bash
pytest tests/test_calc.py::TestCalculator
```

Run a specific method:

```bash
pytest tests/test_calc.py::TestCalculator::test_add_positive_numbers
```

---

Each method in the class represents a test case.


---

## Problem 2: Sharing Setup Logic with Class Fixtures

You want to avoid repeating common test data setup in each method. Use a **class-scoped fixture** to share the same setup across multiple test methods in a class.

---

### Class Fixture Example: `tests/test_calc.py`

```python
import pytest
from app.calc import add, subtract

# Class-scoped fixture
@pytest.fixture(scope="class")
def calc_data():
    print("\n[SETUP] Creating calculator test data...")
    data = {"a": 10, "b": 5}
    yield data
    print("\n[TEARDOWN] Cleaning up calculator test data...")

class TestCalculatorWithFixture:
    def test_add(self, calc_data):
        result = add(calc_data["a"], calc_data["b"])
        assert result == 15

    def test_subtract(self, calc_data):
        result = subtract(calc_data["a"], calc_data["b"])
        assert result == 5
```

---

### Explanation

- The fixture is created **once per class**.
- Both tests use `calc_data` to access the shared dictionary.
- Setup runs once before any test in the class.
- Teardown runs after all tests in the class finish.

---

