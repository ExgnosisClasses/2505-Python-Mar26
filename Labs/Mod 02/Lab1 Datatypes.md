# Lab 2-1 - Python Lab: Exploring Data Types, Immutability, and `id()`


---

##  Part 1: Basic Data Types and `id()`

When you assign the same value to two variables, Python may optimize memory by pointing them to the same object.

#### Try this:

```python
a = 42
b = 42

print("a ID:", id(a))
print("b ID:", id(b))
print("a and b have the same ID:", id(a) == id(b))

s1 = "test"
s2 = "test"
print("s1 and s2 have the same ID:", id(s1) == id(s2))
```

**Explanation**  
- Python caches small integers and short strings. So `a` and `b`, or `s1` and `s2`, may point to the same object in memory.

---

## Part 2: Mutability and Shared References

Lists are **mutable**, so if two variables point to the same list and you change one, the other changes too.

#### Try this:

```python
x = [1, 2, 3]
y = x

print("x ID:", id(x))
print("y ID:", id(y))
print("x and y have the same ID:", id(x) == id(y))

x.append(4)
print("x after append:", x)
print("y reflects change:", y)
```

**Explanation**
- `x` and `y` refer to the **same object**, so any change is visible from both.

---

## Part 3: Copying a Mutable Object

#### Try this:

When you make a copy of a list using `.copy()`, Python creates a new object.

The difference between `==` and `is`?
- `==` checks if values are the same.
- `is` checks if both variables point to the same object.

```python
x = [1, 2, 3]  # Creates an object
y = [1, 2, 3]    # Creates a different object
print("x equals y:", y == x)
print("x is y:", y is x)

z = x.copy()  # Creates a copy

print("x ID:", id(x))
print("z ID:", id(z))

print("z equals x:", z == x)
print("z is x:", z is x)
```

The difference between `==` and `is`?  
- `==` checks if values are the same.  
- `is` checks if both variables point to the same object.

---

## Part 4: Immutability of Strings

Strings in Python are immutable, meaning any change creates a new object.

#### Try this:

```python
msg = "hello"
print("Original msg ID:", id(msg))

msg += " world"
print("New msg:", msg)
print("New msg ID:", id(msg))
```

- The `id()` changes because the new string is a different object in memory.

---

## Part 5: Type Checking

You can use `type()` to check the data type of any value.

#### Try this:

```python
a = 42
f = 32.18
b = True
nada = None
msg = "hello"
x = [1, 2 ,3]

print("Type of 42:", type(a))
print("Type of 32.18:", type(f))
print("Type of True:", type(b))
print("Type of nada:", type(nada))
print("Type of 'hello'", type(msg))
print("Type of [1,2,3]:", type(x))
```

Why is this useful?  
- It helps you understand and debug your code, especially when working with input data or test results.




