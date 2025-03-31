# Lab 8-1 : Understanding Encapsulation, Getters, and Setters in Python

---

## Part 1: The Problem

Imagine you're building a test automation component for login validation. The password entered by the user must:

- Be stored securely
- Not be exposed when accessed
- Be validated before saving

To accomplish this, we’ll use **encapsulation** by:

- Declaring private attributes
- Creating getter and setter methods

---

## Part 2: Your Task

### Step 1 – Define the Class

Create a class `SecureLogin` with:
- A private attribute called `__password`
- A method `set_password(pwd)` that:
    - Sets the password **only** if it is 8 characters or longer
    - Prints a message if the password is too short
- A method `get_password()` that:
    - Returns `"******"` instead of the actual password

---

### Solution

```python
class SecureLogin:
    def __init__(self):
        self.__password = None  # private attribute

    def set_password(self, pwd):
        if len(pwd) >= 8:
            self.__password = pwd
            print("Password set successfully.")
        else:
            print("Password too short! Must be at least 8 characters.")

    def get_password(self):
        return "******"  # Don't return the real password
```

### What Happens When You Run This Code?

```shell
login = SecureLogin()
login.set_password("abc")          # Too short
login.set_password("securePass")   # Valid
print(login.get_password())        # Returns masked output
```

#### Explanation:

`self.__password = None` makes __password a private variable.
- Python name-mangles it internally as `_SecureLogin__password` to prevent accidental access.
- `set_password()` validates the input and stores it if valid.
- `get_password()` protects the actual password from exposure by returning "******".

## Part 3: Testing Direct Access 

Mangling is not encrypting, you can still bypass the encapsulation if you need to by using the following code.
- This is not recommended except for debugging since it defeats the purpose of encapsulation


```python
print(login._SecureLogin__password)  # Works, but breaks encapsulation
```

## Part 4: Customize It – Bonus Task

Extend the SecureLogin class:
- Add a username attribute
- Add get_username() and set_username(name) methods

```python
class SecureLogin:
    def __init__(self):
        self.__password = None
        self.username = None

    def set_password(self, pwd):
        if len(pwd) >= 8:
            self.__password = pwd
            print("Password set.")
        else:
            print("Too short!")

    def get_password(self):
        return "******"

    def set_username(self, name):
        self.username = name

    def get_username(self):
        return self.username

```

Test it

```python
login = SecureLogin()
login.set_password("securePass")   # Valid
print(login.get_password())  
login.set_username("Zorgo")   # Valid
print(login.get_username())  

```

