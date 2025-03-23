# Lab 3-3 Sets and Dictionaries

In this lab, you’ll solve real-world problems using two powerful Python data structures:
- `set`: for handling **unique values** and **fast membership checking**
- `dict`: for managing **key-value pairs** and **structured data**

---

## Part 1: Working with Sets

### Problem:
You received logs from a test suite that recorded duplicate failures. You need to find the **unique error types**.

```python
log_errors = [
    "timeout", "connection lost", "disk full", "timeout",
    "disk full", "authentication failed", "timeout"
]
```

### Solution:
```python
unique_errors = set(log_errors)
print("Unique errors:", unique_errors)
```

###  Why it works:
- A `set` automatically removes duplicates.
- It is **unordered** and only stores **unique values**.
- Very useful for cleaning up noisy test logs.

---

### Bonus: Check if a Specific Error Occurred

```python
if "disk full" in unique_errors:
    print("Disk space issue detected")
```

Sets support **fast membership tests** – faster than searching a list!

---

## Part 2: Working with Dictionaries

### Problem:
You want to track how many times each test case ran in a repeated test loop.

```python
test_runs = ["TC001", "TC002", "TC001", "TC003", "TC002", "TC001"]
```

### Solution:
```python
run_counts = {}

for test_id in test_runs:
    run_counts[test_id] = run_counts.get(test_id, 0) + 1

print("Test run counts:", run_counts)
```

### Why it works:
- `dict.get(key, default)` avoids key errors.
- A dictionary tracks the **frequency** of each test case.
- Excellent for summarizing repeated test execution.

---

### Bonus: Sort Tests by Run Count

We will look in more detail into what is going on in this code in the next module.

```python
sorted_counts = dict(sorted(run_counts.items(), key=lambda x: x[1], reverse=True))
print("Sorted by frequency:", sorted_counts)
```

This is useful for prioritizing high-usage or flaky tests for further analysis.

---

## Part 3: Nested Dictionaries – Tracking Detailed Test Info

### Problem:
You want to store the **status and duration** of multiple test cases. Create a dictionary where each key is a test ID, and each value is another dictionary with keys `"status"` and `"duration"`.

```python
test_data = {
    "TC001": {"status": "PASS", "duration": 1.2},
    "TC002": {"status": "FAIL", "duration": 0.9},
    "TC003": {"status": "SKIP", "duration": 0.0}
}
```

### Access and Update Values:
```python
# Access status of TC002
print("TC002 status:", test_data["TC002"]["status"])

# Update duration of TC003
test_data["TC003"]["duration"] = 1.0
print("Updated TC003:", test_data["TC003"])
```

**Why it works**:
- You’re accessing nested values with `dict[key][nested_key]`.
- Useful when tracking rich metadata per test case.

---

## Part 4: Set Operations – Comparing Test Results

### Problem:
You want to compare test results from two different runs and identify:
- Tests that passed in both
- Tests that failed in the second run only
- Tests missing from the second run

```python
run1_passed = {"TC001", "TC002", "TC003", "TC005"}
run2_passed = {"TC002", "TC003", "TC004"}
all_tests = {"TC001", "TC002", "TC003", "TC004", "TC005", "TC006"}
```

### Solution:
```python
# Passed in both runs
common_passes = run1_passed & run2_passed
print("Passed in both runs:", common_passes)

# Passed in run1 but not in run2
regressions = run1_passed - run2_passed
print("Regressions (passed before, not now):", regressions)

# Tests missing from second run
missing_in_run2 = all_tests - run2_passed
print("Tests missing in run2 results:", missing_in_run2)
```

### Explanation:
| Operation           | Symbol | Description                              |
|---------------------|--------|------------------------------------------|
| Intersection        | `&`    | Common elements                          |
| Difference          | `-`    | Elements in one set, not the other       |
| Union               | `|`    | All unique elements from both sets       |



---