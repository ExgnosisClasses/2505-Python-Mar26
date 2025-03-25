# Lab 4-2: Understanding Variable Scope

In this lab, you'll learn how Python handles variable scope through practical examples. You'll explore local, global, and nested scopes and see how variables behave in different parts of your program.


---

## Part 1: Local Scope

### Problem:
Create a function that defines a local variable. Try to access the variable outside the function.

```python
def run_test():
    result = "PASS"
    print("Inside function:", result)

run_test()

# Try accessing result outside the function
try:
    print("Outside function:", result)
except NameError as e:
    print("Error:", e)
```

### Explanation:
- `result` exists only inside the function.
- Accessing it outside results in a `NameError`.

---

## Part 2: Global Scope

### Problem:
Create a global variable and access it inside a function.

```python
status = "READY"

def check_status():
    print("Status is:", status)

check_status()
```

### Explanation:
- Variables defined outside a function are in the **global scope**.
- Functions can read global variables, but can’t modify them without a special declaration.

---

## 🔹 Part 3: Modifying Global Variables

### Problem:
Try to modify a global variable inside a function.

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print("Counter:", counter)
```

### Explanation:
- To change a global variable inside a function, you must use the `global` keyword.
- Without `global`, Python would treat `counter` as a new local variable and raise an error.

---

## Part 4: Enclosing Scope (Nested Functions)

### Problem:
Define a function inside another function and use a variable from the outer (enclosing) function.

```python
def outer():
    message = "Running"
    def inner():
        print("Message is:", message)
    inner()

outer()
```

### Explanation:
- The inner function can access variables from its enclosing function.
- This is called a **closure** or **enclosing scope**.

---

## Part 5: Variable Shadowing

### Problem:
What happens if you define a variable with the same name in a local and a global scope?

```python
name = "Global"

def greet():
    name = "Local"
    print("Inside function:", name)

greet()
print("Outside function:", name)
```

### Explanation:
- The local variable `name` **shadows** the global variable.
- The global variable remains unchanged.

---

## Bonus: Combining Scopes

### Problem:
Define a nested function that modifies a variable from an outer (non-global) scope using `nonlocal`.

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print("Inner count:", count)
    inner()
    print("Outer count:", count)

outer()
```

### Explanation:
- `nonlocal` allows you to modify a variable in an enclosing (but non-global) scope.
- This is useful in nested functions and closures.

---


