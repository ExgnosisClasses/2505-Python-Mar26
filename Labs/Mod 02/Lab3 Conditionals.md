# Lab 2-3: Conditionals

In this lab, you'll learn how to use conditional statements (`if`, `elif`, `else`) in Python to solve testing-related problems. You'll work with two common structures:
1. Multi-branch conditionals
2. Nested conditionals

Each section presents a practical scenario and includes a solution.


## 🔹 Part 1: Multi-Branch Conditional with `elif`

### Problem:
You're checking the status of a test case based on a numeric response code. Use a multi-branch conditional to print the appropriate status message:

- 200 → "OK – Test Passed"
- 404 → "Not Found – Test Failed"
- 500 → "Server Error – Test Crashed"
- Any other code → " Unknown Status"

###  Solution:
```python
response_code = 404  # Change this value to test different paths

if response_code == 200:
    print("OK – Test Passed")
elif response_code == 404:
    print("Not Found – Test Failed")
elif response_code == 500:
    print("Server Error – Test Crashed")
else:
    print("Unknown Status")
```

**What’s Happening?**
- Python evaluates each condition from top to bottom.
- Only the first `True` condition is executed.
- If none match, the `else` block runs.

---

## Part 2: Nested `if` Statements

### Problem:
You are analyzing test data from a login test. The test only passes if the username is valid **and** the login is successful. Use nested `if` statements to model this logic.

- If `username_valid` is True:
    - If `login_successful` is True → "Login successful"
    - Else → "Login failed"
- Else → "Invalid username"

### Solution:
```python
username_valid = True
login_successful = False

if username_valid:
    if login_successful:
        print("Login successful")
    else:
        print("Login failed")
else:
    print("Invalid username")
```

 **What’s Happening?**
- The outer `if` checks if the username is valid.
- Only if that passes, the inner `if` checks login status.

---

## Reflection

- What happens if both `username_valid` and `login_successful` are `False`?
- Try replacing the nested `if` with `if`/`elif`/`else`. Does it make the code clearer or more confusing?

---

## Summary

In this lab, you:
- Used multi-branch conditionals to handle multiple discrete outcomes
- Used nested conditionals to represent dependencies between conditions


