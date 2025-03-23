# LAb 3-4 : Shallow vs Deep Copy

In this lab, you’ll explore the difference between **shallow copies** and **deep copies** in Python, especially when working with **nested data structures** like lists of lists or dictionaries of dictionaries.

Understanding this difference is essential when writing tests that duplicate or reuse test data structures without unintended side effects.

---

## Part 1: Shallow Copy with Nested Lists

### Problem:
You want to make a copy of a list of test steps, where each step includes a name and parameters.

```python
import copy

original = [["login", {"user": "admin"}], ["upload", {"file": "report.csv"}]]

shallow = copy.copy(original)
shallow[0][1]["user"] = "guest"

print("Original:", original)
print("Shallow Copy:", shallow)
```

### Explanation:
- `copy.copy()` creates a **new outer list**, but its **inner objects (lists/dicts)** are still shared.
- Changing one affects the other — this is the behavior of a **shallow copy**.

---

## Part 2: Deep Copy with Nested Lists

### Problem:
You want a **completely independent copy** of the nested test data.

```python
deep = copy.deepcopy(original)
deep[1][1]["file"] = "logs.zip"

print("Original (unchanged):", original)
print("Deep Copy:", deep)
```

### Explanation:
- `copy.deepcopy()` creates **new inner objects** too.
- The original remains unchanged — this is a **true copy** of the entire structure.

---

## 🔹 Part 3: Shallow Copy with Nested Dictionary

### Problem:
You are copying a dictionary of test configurations but only using a shallow copy.

```python
test_config = {
    "env": "staging",
    "options": {
        "retries": 3,
        "timeout": 5
    }
}

shallow_copy = copy.copy(test_config)
shallow_copy["options"]["retries"] = 0

print("Original config:", test_config)
print("Shallow config:", shallow_copy)
```

### Explanation:
- The inner `"options"` dictionary is shared.
- A change in one copy reflects in both.


### Solution: Use deep copy

```python
test_config = {
    "env": "staging",
    "options": {
        "retries": 3,
        "timeout": 5
    }
}

deep_copy = copy.deepcopy(test_config)
deep_copy["options"]["retries"] = 0

print("Original config:", test_config)
print("Shallow config:", deep_copy)
```
---

## Summary Table

| Feature         | `copy.copy()`              | `copy.deepcopy()`           |
|-----------------|----------------------------|------------------------------|
| Top-level copy  |  Yes                      |  Yes                       |
| Nested copy     |  No (shared references)   |  Yes (full duplication)    |
| Safe to modify  |  No (may change original) | Yes (fully independent)    |

---

## Real-World Use Case for Testers

When duplicating:
- Test step templates
- Configuration trees
- Test result payloads

Always use `deepcopy()` when:
- You need an independent copy that won't interfere with the original
- You’re manipulating nested data structures in parallel test scenarios

