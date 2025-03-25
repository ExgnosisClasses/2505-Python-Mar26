# LAb 4-3 Closures and Decorators

# 🧪 Python Lab: Closures and Decorators


## Part 1: Closures – Retaining State Between Calls

### Problem:
You want to track how many test steps have been completed, but without using a global variable. Create a function that remembers how many times it has been called.

### Solution:
```python
def test_step_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return f"Step {count} complete"

    return increment

step_tracker = test_step_counter()
print(step_tracker())  # Step 1 complete
print(step_tracker())  # Step 2 complete
print(step_tracker())  # Step 3 complete
```

### Explanation:
- `increment()` is a **closure**: it has access to the `count` variable even after `test_step_counter()` finishes.
- `nonlocal` is required to modify `count` from the enclosing scope.
- This is useful for tracking test state without global variables.

---

## Part 2: Decorators – Enhancing a Function

### Problem:
You want to log whenever a test function runs, but without editing the original function. Create a decorator that prints a log message before and after running the function.

### Solution:
```python
def log_test(func):
    def wrapper(*args, **kwargs):
        print(f"Starting test: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished test: {func.__name__}")
        return result
    return wrapper

@log_test
def run_login_test():
    print("Running login test logic...")

run_login_test()
```

### Explanation:
- `@log_test` wraps the `run_login_test()` function with additional behavior.
- The `wrapper()` function executes before and after the original function.
- This is a common pattern for logging, error handling, and instrumentation.

---



