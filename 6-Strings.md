# 6 - Strings



This module introduces you to working with strings in Python, focusing on real-world tasks that software testers encounter—like validating output, parsing logs, and formatting test results.

---

## String Basics

### Defining Strings

You can define strings with single, double, or triple quotes.

```python
a = 'Hello'
b = "World"
c = '''This is a
multiline string'''
```

Use **triple quotes** for multi-line text or docstrings.

### Escape Characters

Escape characters allow special formatting:

```python
print("Line 1\nLine 2")   
print("Name\tResult")    
```

### Raw Strings

A raw string is a string where backslashes (\) are treated as literal characters and not as escape characters.

You create a raw string by prefixing the string with r or R:

Useful when working with regex or file paths:

```python
path = r"C:\Tests\output.txt"
print(path)  # C:\Tests\output.txt
```

---

## String Indexing and Slicing

### Indexing

Indexing works the same as with lists, but you cant do something `s[0]="a"`

```python
s = "Python"
print(s[0])    # 'P'
print(s[-1])   # 'n'
```

### Slicing

```python
print(s[1:4])    # 'yth'
print(s[:3])     # 'Pyt'
print(s[::2])    # 'Pto'
```

Useful for extracting parts of strings like test IDs, status codes, or dates.

---

## String Methods

### Cleaning Input

Stripping off leading and trailing whitespace

```python
s = "  pass  "
print(s.strip())   # 'pass'
```

### Case Conversion

```python
print("fail".upper())  # 'FAIL'
print("PASS".lower())  # 'pass'
```

### Searching and Splitting

```python
log = "Test TC001 passed"
print(log.startswith("Test"))    # True
print(log.find("TC001"))         # 5
print(log.split())               # ['Test', 'TC001', 'passed']
```

### Replacing and Joining

```python
s = "FAIL,FAIL,PASS"
print(s.replace("FAIL", "RETRY", 1))  # 'RETRY,FAIL,PASS'

parts = ["TC001", "PASS"]
print(":".join(parts))  # 'TC001:PASS'
```

---

## String Formatting and Interpolation

### Using f-strings (recommended)

```python
test_id = "TC001"
status = "PASS"
print(f"{test_id} - Result: {status}")
```

### Old-style (% formatting)

```python
print("Test %s: %s" % (test_id, status))
```

### Using .format()

```python
print("Test {}: {}".format(test_id, status))
```

### Padding and Alignment

```python
print(f"{'Test':<10}{'Result':>10}")  # Left and right align
```

---

## String Comparisons and Membership

### Comparing Strings

```python
expected = "pass"
actual = "PASS"
print(expected.lower() == actual.lower())  # True
```

### Membership Checks

```python
msg = "Test completed successfully"
print("success" in msg)  # True
```

---

## Multiline and Multi-part Strings

### Multiline Text

```python
log = '''Start test
Log in
Run checks
Log out'''
print(log.splitlines())
```

### ✅ Combining Strings

```python
lines = ["Line1", "Line2", "Line3"]
print("\n".join(lines))
```

---

## Regular Expressions (Intro)

### Using `re` to Search

```python
import re
log = "Test TC101 completed"
match = re.search(r"TC\d+", log)
if match:
    print(match.group())  # TC101
```

---

## Common Tasks for Testers

### Parse Test ID from Log

```python
line = "Test TC001 passed"
test_id = line.split()[1]
print(test_id)  # TC001
```

### Check Output Contains Expected Substring

```python
response = "Status: OK, Code: 200"
assert "200" in response
```

---

## Best Practices

- Use `strip()` and `lower()` to normalize strings before comparing
- Use `join()` instead of `+` in loops
- Use raw strings for file paths and regex
- Avoid assuming fixed string positions unless format is guaranteed

