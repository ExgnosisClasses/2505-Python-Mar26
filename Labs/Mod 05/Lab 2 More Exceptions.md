# Lab 5-2: Raising and Handling Custom Exceptions

---

## Part 1: Raising Exceptions Manually

### Problem:
You want to reject invalid test input and stop execution if a condition isn’t met.

### Solution:

```python
def check_positive(value):
    if value < 0:
        raise ValueError("Test value must be positive.")

check_positive(-5)
```

### Explanation:
- `raise` is used to manually throw an exception when input validation fails.
- Helps enforce rules in your test scripts.

---

##  Part 2: Using `raise AssertionError` for Test Failures

### Problem:
You want to report a test failure with a clear message using `raise`.

### Solution:

```python
def validate_status(status):
    if status != "PASS":
        raise AssertionError(f"Test failed: status was {status}")

validate_status("FAIL")
```

### Explanation:
- `raise AssertionError` gives control over test output and custom failure messaging.
- Unlike `assert`, this will always run and cannot be disabled with Python optimizations.

---

## Part 3: Creating Custom Exception Classes

### Problem:
You want to represent a specific kind of test failure with a named exception.

###  Solution:

```python
class LoginTimeoutError(Exception):
    pass

def login():
    raise LoginTimeoutError("Login test failed: timeout occurred")

try:
    login()
except LoginTimeoutError as e:
    print(f"❌ Custom error: {e}")
```

### Explanation:
- Custom exceptions clarify what kind of error occurred.
- Makes your test framework more expressive and maintainable.

---

## Part 4: Exception Propagation and Re-Raising

### Problem:
You want to catch and log an exception in a helper function but still raise it so the test fails properly.

### Solution:

```python
def check_field():
    try:
        raise KeyError("Missing test field")
    except KeyError as e:
        print(f"Logged error: {e}")
        raise  # Re-raises the original exception

def run_test():
    check_field()

run_test()
```

### Explanation:
- `raise` (by itself) re-raises the most recent exception.
- Useful when logging or cleanup must occur but the test should still fail.

---

## Part 5: Best Practices for Testers

### Problem:
You want to catch errors in a specific test step but allow unexpected exceptions to bubble up.

### Solution:

```python
def step():
    raise TimeoutError("Step took too long")

try:
    step()
except TimeoutError as e:
    print(f"Step failed: {e}")
```

### Explanation:
- Catch only specific exceptions that you plan to handle.
- Let unexpected exceptions bubble up so they aren’t silently ignored.

---

