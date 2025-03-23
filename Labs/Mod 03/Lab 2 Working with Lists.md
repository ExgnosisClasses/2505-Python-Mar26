 # Lab 3-2: Indexing, Slices, and List Comprehensions (New Examples)


## Part 1: List and Tuple Indexing

### Problem:
You have a list of error messages and a tuple of log levels. Access the second error message and the last log level.

```python
error_messages = ["Timeout error", "Authentication failed", "Disk full", "Connection reset"]
log_levels = ("DEBUG", "INFO", "WARNING", "ERROR")
```

### Solution:
```python
print("Second error message:", error_messages[1])
print("Last log level:", log_levels[-1])
```

### Why it works:
- Index `1` gives the second element (remember, counting starts at 0).
- `-1` is the shortcut to access the last item in an ordered collection.

---

## Part 2: Slicing Lists and Tuples

### Problem:
You are analyzing a test run and want to:
- Extract the **middle three** results from a list of durations
- Reverse a tuple representing the test stages

```python
durations = [0.2, 1.5, 3.1, 4.7, 2.0, 0.9]
stages = ("setup", "run", "verify", "teardown")
```

### ✅Solution:
```python
# Middle three durations (index 1 to 3 inclusive)
middle = durations[1:4]
print("Middle durations:", middle)

# Reverse the tuple
reversed_stages = stages[::-1]
print("Reversed stages:", reversed_stages)
```

###  Why it works:
- Slicing uses `start:stop`, where `stop` is **exclusive**.
- `[::-1]` creates a reversed copy of the tuple.

---

## Part 3: List Comprehensions

### Problem:
You want to:
1. Generate test user emails from a list of usernames
2. Extract only lowercase usernames from a mixed list

```python
usernames = ["admin", "GUEST", "qa_lead", "TESTER"]
```

### Solution:
```python
# Generate email addresses
emails = [f"{user}@testlab.com" for user in usernames]
print("Emails:", emails)

# Extract lowercase usernames
lowercase_users = [u for u in usernames if u.islower()]
print("Lowercase only:", lowercase_users)
```

### Why it works:
- The expression `f"{user}@testlab.com"` builds each email string.
- `u.islower()` checks if the entire username is lowercase.

---