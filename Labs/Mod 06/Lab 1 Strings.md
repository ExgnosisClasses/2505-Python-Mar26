# Lab 6-1: Working with Strings

---

## String Basics and Escape Characters

### Problem:
You need to store a string that includes both quotes and a newline. Create and print this string.

### Solution:

```python
message = '''"She said, "Testing starts now.
Begin execution."'''
print(message)
```

### Explanation:
- ''' ... ''' allows a double quote inside a string.
- Saves newline as a character in the string

---

## String Indexing and Slicing

### Problem:
Given the string `"TC045:LoginTest:PASS"`, extract:
- The test ID (`TC045`)
- The test name (`LoginTest`)
- The result (`PASS`)

### Solution:

```python
record = "TC045:LoginTest:PASS"
parts = record.split(":")
test_id = parts[0]
test_name = parts[1]
result = parts[2]

print(test_id, test_name, result)
```

### Explanation:
- `split(":")` separates the string into a list using `:` as the delimiter.

---

## String Methods

### Problem:
A test name has extra spaces and inconsistent casing. Normalize it.

```python
raw_name = "   logintestCASE001   "
```

### Solution:

```python
clean_name = raw_name.strip().upper()
print(clean_name)  # LOGINTESTCASE001
```

### Explanation:
- `strip()` removes whitespace.
- `upper()` converts the string to uppercase.

---

## String Formatting

### Problem:
Generate a result summary using variables for the test ID and result, formatted as:

```
Test TC102 completed with status: FAIL
```

### Solution:

```python
test_id = "TC102"
status = "FAIL"
summary = f"Test {test_id} completed with status: {status}"
print(summary)
```

### Explanation:
- `f-strings` let you embed variables directly into strings for clean formatting.

---

## String Comparison and Membership

### Problem:
Check whether the message `"Connection Error: Timeout"` includes the word `"timeout"`, case-insensitively.

### Solution:

```python
message = "Connection Error: Timeout"
if "timeout" in message.lower():
    print("Found timeout issue.")
```

### Explanation:
- Converting to `lower()` ensures the match is case-insensitive.

---

## Combining Strings and Multiline

### Problem:
You want to create a multiline string representing the steps in a test case and count the number of steps.

### Solution:

```python
steps = '''
'''.join(["Open browser", "Navigate to URL", "Login", "Run check", "Logout"])
print(steps)
print("Number of steps:", steps.count("\n") + 1)
```

### Explanation:
- `join()` combines list items into one string.
- `count("\n") + 1` gives the number of lines.

---

## Using Raw Strings

### Problem:
Write a file path to a log file without escaping backslashes.

### Solution:

```python
log_path = r"C:\log\test_output.log"
print(log_path)
```

### Explanation:
- Raw strings (`r"..."`) preserve backslashes, making Windows paths and regex easier to write.

---

## Common Testing Use Case

### Problem:
Given a response message, extract the numeric code from `"Response Code: 503"`.

### Solution:

```python
msg = "Response Code: 503"
code = msg.split(":")[1].strip()
print(code)  # 503
```

### Explanation:
- `split(":")` separates key/value.
- `strip()` removes extra spaces.

-
