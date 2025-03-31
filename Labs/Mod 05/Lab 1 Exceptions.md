# Lab 5-1: Exception Handling for Testers


---

## Part 1: General Exception Handling

### Problem:
Your test crashes when dividing numbers, and you want to prevent it from failing if the input is bad.

### Solution:

```python
print("Starting test...")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

### Explanation:
The `try` block runs the risky code. The `except` catches the error and handles it gracefully.

---

## Part 2: Common Built-in Exceptions

### Problem:

You’re loading test input from a file and performing data validation.

The data is numberic but stored as strings in the file

Identify which exceptions need to be handled.

### Solution:

```python
try:
    with open("input.txt") as f:
        data = f.read()
        value = int(data)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Input is not a valid integer.")
```

### Explanation:
- `FileNotFoundError` handles missing files.
- `ValueError` handles invalid input conversion.

---

## Part 3: Basic Try-Except Blocks

### Problem:
You are parsing test configuration values and need to handle multiple error types.

### Solution:

```python
config = None

try:
    print(config["timeout"])  # This will fail
except (TypeError, KeyError) as e:
    print(f"Error reading config: {e}")
```

### Explanation:
- `TypeError` is raised because `config` is `None`
- `KeyError` would be raised if `timeout` was missing from a dict
- Multiple exceptions can be caught in a single `except` block

---

### Problem:
You want to catch all unexpected errors during a test run.

### Solution:

```python
def run_test():
    try:
        result = 5 / 0
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

run_test()
```

### Explanation:
Use `except Exception` to catch any error, especially useful in test runners or logging wrappers.

---

## Part 4: Using `else` and `finally`

### Problem:
You want to log a success message only if no errors occur, and always clean up resources afterward.

### Solution:

```python
def validate_input(value):
    try:
        result = int(value)
    except ValueError:
        print("Not a valid number.")
    else:
        print("Input converted successfully.")
    finally:
        print("Finished checking input.")

validate_input("42")
validate_input("oops")
```

### Explanation:
- `else` runs only if the `try` block completes successfully.
- `finally` always runs—great for cleanup tasks or teardown logic.

---
