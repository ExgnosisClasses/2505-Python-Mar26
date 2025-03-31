# Lab 8-2: Lab: Inheritance

## Part 1: The Problem

In real-world testing automation, you often have shared test behaviors (like logging or generating reports) across different types of tests. Instead of rewriting the same logic, we can use **inheritance** to define shared behavior in base classes and extend it in specialized classes.

---

## Part 2: Your Task

You will build a set of classes to simulate test execution. You’ll:
- Define a base class with a generic `run()` method
- Create subclasses for specific test types
- Add another class to handle logging
- Use multiple inheritance and see how Python decides which method to run

---

## Step 1 – Single Inheritance

###Define a base class and a child class

```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running test case: {self.name}")

class LoginTest(TestCase):
    def validate(self):
        print("Validating login functionality")

```

Test the code

```python
lt = LoginTest("Login Test 001")
lt.run()         # Inherited from TestCase
lt.validate()    # Defined in LoginTest
```


## Step 2 – Method Overriding

Redefine the `run()` method in the child class so that it overrides the parent method

```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running test case: {self.name}")

class LoginTest(TestCase):
    def validate(self):
        print("Validating login functionality")

    def run(self):
        print(f"Running login-specific test: {self.name}")

lt = LoginTest("Login Test 002")
lt.run() 

```

- The run() method in LoginTest overrides the one from TestCase
- When you call run() on a LoginTest object, Python uses the child’s version


## Step 3 – Use super() to Extend the Parent Method

Have the child run() method add more functionality to the parent run() method

```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running test case: {self.name}")

class LoginTest(TestCase):
    def validate(self):
        print("Validating login functionality")

    def run(self):
        super().run()  # Calls the base class version
        print("Extra login validation logic...")
        
lt = LoginTest("Login Test 002")
lt.run()

```
## Step 4 – Multiple Inheritance

Add a separate class for logging
```python
class LogHandler:
    def generate(self):
        print("Logging test execution...")

class ReportGenerator:
    def generate(self):
        print("Generating test report...")

```
Now create a utility class that inherits from both:

```python
class TestUtility(ReportGenerator, LogHandler):
    pass

tu = TestUtility()
tu.generate()
```

Explanation:
- TestUtility inherits from both ReportGenerator and LogHandler
- Python uses method resolution order (MRO) to decide which generate() to run
- It looks in ReportGenerator first, so that version is called

View Method Resolution Order (MRO)

```python
print(TestUtility.__mro__)
```
```shell
(<class '__main__.TestUtility'>, <class '__main__.ReportGenerator'>, <class '__main__.LogHandler'>, <class 'object'>)
```

Python checks classes left-to-right when resolving methods.

## Step 5 – Switch the Inheritance Order

```python
class TestUtility(LogHandler, ReportGenerator):
    pass

tu = TestUtility()
tu.generate()
```

```shell
Logging test execution...
```

- Now LogHandler is checked first, so its version of generate() is used

Reflection Questions
- What happens if both parent classes have a method with the same name?
- How does Python decide which one to use?
- Why is multiple inheritance something to use carefully in test automation?

## Optional Practice Task

Build the following class structure:
- BaseTest with a run() method that prints "Running base test...".
- UITest that inherits from BaseTest and overrides run() to print "Running UI test...".
- Logger with a method log_result() that prints "Saving test logs...".
- FullTest that inherits from both UITest and Logger.

Instantiate a FullTest object and call:
- run() → should use UITest version
- log_result() → from Logger
- Use super() to call the base test logic inside the overridden run() method

#### Solution

```python
# 1. Base class with a run method
class BaseTest:
    def run(self):
        print("Running base test...")

# 2. Subclass that overrides the run method
class UITest(BaseTest):
    def run(self):
        super().run()  # Call the base class's run method
        print("Running UI test...")

# 3. Separate class with its own method
class Logger:
    def log_result(self):
        print("Saving test logs...")

# 4. Class that inherits from both UITest and Logger
class FullTest(UITest, Logger):
    pass

# Create an object of FullTest
test = FullTest()

# Call the overridden run method
test.run()

# Call the Logger method
test.log_result()

```



