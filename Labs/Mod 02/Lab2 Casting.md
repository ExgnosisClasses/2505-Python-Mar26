# Lab 2-2: Type Casting, None Type, and Variable Use

This lab introduces how to work with different data types in Python using real-world testing scenarios. You'll practice:

- Implicit and explicit type casting
- Handling missing values using `None`
- Declaring and using variables to store test data

---

## Part 1: Implicit and Explicit Type Casting

Python sometimes converts values automatically (implicit), and sometimes you must do it manually (explicit).

### Step 1: Implicit Casting

```python
# Combining int and float in an operation
response_code = 200
timeout_seconds = 0.5

total = response_code + timeout_seconds

print("Total value:", total)
print("Type of total:", type(total))
```

**Explanation**:  
Python automatically converts `200` (int) to `200.0` (float) during addition.

---

###  Step 2: Explicit Casting

```python
# Converting a string to an integer
response_time = "150"  # string from input or API
threshold = 200

if int(response_time) < threshold:
    print("Response time is acceptable.")
else:
    print("Response time is too high.")
```

**Explanation**:  
`int(response_time)` converts the string `"150"` into an integer so you can compare it to another number.

---

## Part 2: Using `None` for Missing Data

Python uses `None` to represent missing or undefined values.

### Step 1: Check if a value is None

```python
username = None  # Failed to extract username from page

if username is None:
    print("Username is missing – Test failed")
else:
    print("Username is:", username)
```

**Explanation**:  
Use `is None` to test if a value has not been set. This is common when working with optional fields.

---

### Step 2: Conditional assignment

```python
# Simulating a data retrieval
def get_email():
    return None  # Imagine the value wasn't found

email = get_email()

if email is None:
    email = "unknown@example.com"

print("Email used for report:", email)
```

**Explanation**:  
Fallback logic is common in tests when optional data is missing.

---

## Part 3: Declaring and Using Variables

In Python, you don’t need to declare types. Just assign values and use them.

### Step 1: Store and display test case info

```python
test_name = "Login Test"
expected = "PASS"
actual = "FAIL"

print("Test Case:", test_name)
print("Expected Result:", expected)
print("Actual Result:", actual)
```

---

###  Step 2: Use variables in a conditional check

```python
if expected == actual:
    print("Test passed!")
else:
    print("Test failed.")
```

**Explanation**:  
You can use variables in `if` statements to make decisions based on test outcomes.

---


