# Lab 2-4: Loops

In this lab, you will practice solving real-world problems using different types of loops in Python. Each section presents a practical problem followed by a solution and explanation.

---

## Part 1: For Loop Over a Collection

### Problem:
You have a list of test cases, and you want to count how many were executed.

###  Solution:
```python
test_cases = ["TC001", "TC002", "TC003", "TC004"]
count = 0

for case in test_cases:
    count += 1

print("Total test cases executed:", count)
```

**Explanation**:
- The `for` loop goes through each item.
- The `count` is incremented for every iteration.

---

## Part 2: For Loop with `range()`

### Problem:
You need to simulate 5 retry attempts for a flaky test step.

### Solution:
```python
for attempt in range(1, 6):
    print(f"Retry attempt #{attempt}")
```

**Explanation**:
- `range(1, 6)` gives numbers 1 through 5.
- Useful when repeating a step a specific number of times.

---

## Part 3: For Loop with `enumerate()`

### Problem:
You have a list of test steps and want to print them with step numbers.

### Solution:
```python
steps = ["Open app", "Login", "Run report", "Logout"]

for index, step in enumerate(steps, start=1):
    print(f"Step {index}: {step}")
```

 **Explanation**:
- `enumerate()` gives you both index and value.
- `start=1` makes the steps start from 1 instead of 0.

---

## Part 4: While Loop

### Problem:
Retry a network check up to 3 times or until successful.

### Solution:
```python
attempts = 0
success = False

while attempts < 3 and not success:
    print(f"Checking network (Attempt {attempts + 1})...")
    if attempts == 2:  # Simulate success on third try
        success = True
        print("Network check passed")
    attempts += 1
```

**Explanation**:
- The `while` loop continues until the success condition is met or max attempts is reached.

---

## Part 5: Break and Continue in Nested Loops

### Problem:
Loop through environments and users. If a user causes a critical error, skip to the next environment.

### Solution:
```python
environments = ["staging", "qa"]
users = ["admin", "guest", "test_user"]

for env in environments:
    print(f"Testing environment: {env}")
    for user in users:
        if user == "test_user":
            print("--- Skipping unstable user test.")
            continue  # Skip this user
        print(f"  Running as {user}")
        if user == "guest" and env == "qa":
            print("   !!! Critical error – exiting loop.")
            break  # Exit inner loop
    print("Finished environment:", env)
```

**Explanation**:
- `continue` skips one user.
- `break` exits the inner loop but not the outer one.

---

## Part 6: Using `else` with a Loop

### Problem:
Search for a failed test case. If none is found, report that all passed.

### Solution:
```python
results = ["PASS", "PASS", "PASS"]

for result in results:
    if result == "FAIL":
        print("Test failed.")
        break
else:
    print("All tests passed.")
```

**Explanation**:
- The `else` block runs **only** if the loop finishes without a `break`.
- Great for search/validation logic.



