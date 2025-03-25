# Lab 4-1: Functions, Lambdas, and First-Class Behavior

In this lab, you'll explore how Python treats functions as first-class objects. You'll define functions using both `def` and `lambda`, assign them to variables, pass them as arguments, and use default and keyword parameters. You'll also examine what happens when a function returns `None`, and as a bonus, see how `yield` creates a generator.

---

## Part 1: Defining Functions with `def` and `lambda`, and Viewing Memory Locations

###  Problem:
Define a named function and a lambda, and observe that they are objects stored in memory.

```python
def greet():
    return "Hello from def!"

shout = lambda: "Hello from lambda!"

print(greet)
print(id(greet))
print(shout)
print(id(shout))
```

### Explanation:
- Functions are objects.
- Printing the function (without `()`) shows its **memory location**.
- The output will look something like `<function greet at 0x...>`

---

## Part 2: Assigning Functions to Variables

### Problem:
Assign an existing function to a new variable and execute it.

```python
def say_hi():
    return "Hi!"

new_func = say_hi
print(new_func())  # Should print "Hi!"
```

### Explanation:
- `new_func` is now another name for the same function.
- Functions can be reassigned just like other variables.

---

## Part 3: Using Functions as Arguments and Return Values

### Problem:
Write a function that takes another function as a parameter and returns a lambda.

```python
def run_test(step_function):
    print("Running:", step_function())

def make_step(step_name):
    return lambda: f"Executing {step_name}"

step = make_step("Login")
run_test(step)
```

###  Explanation:
- `run_test` accepts a function and calls it.
- `make_step` returns a lambda (anonymous function) that closes over a variable.

---

## Part 4: When `None` Is the Return Value

### Problem:
Create a function that prints a message but doesn’t explicitly return anything.

```python
def log_result(result):
    print(f"Result: {result}")

response = log_result("PASS")
print(response)  # Should print None
```

### Explanation:
- If a function has no `return` statement, Python automatically returns `None`.

---

## Part 5: Functions Using Keyword and Default Arguments

### Problem:
Write a function with default values and call it using positional and keyword arguments.

```python
def report_status(test="TC001", status="PASS"):
    return f"Test {test} finished with status: {status}"

print(report_status())  # Uses both defaults
print(report_status("TC002"))  # Override test
print(report_status(status="FAIL"))  # Override keyword only
```

### Explanation:
- Default parameters make arguments optional.
- Keyword arguments allow flexible and readable function calls.

---

## Bonus: Using `yield` to Create a Generator

### Problem:
Create a generator that yields multiple test IDs one by one.

```python
def generate_test_ids():
    for i in range(3):
        yield f"TC{i:03}"

for test_id in generate_test_ids():
    print(test_id)
```

### Explanation:
- `yield` turns the function into a generator.
- The function pauses after each `yield`, resuming on the next iteration.
- Useful for **streaming test data or logs**.

---

