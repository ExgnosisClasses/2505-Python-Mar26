# Lab 8-3: Understanding Polymorphism in Python


---

## Part 1: The Problem

In a real-world testing framework, you might have different types of tests — like UI tests, API tests, or database tests. 
- Even though these tests behave differently, you often want to treat them all the same way in your test runner.

Using **polymorphism**, you can:
- Define a shared method name (`run()`)
- Allow each subclass to implement its own behavior
- Call the same method across objects of different types

---

##  Part 2: Your Task

You’ll:
- Define a base class with a generic method
- Create multiple subclasses that override that method
- Run all test objects using a shared function — demonstrating polymorphism

---

## Step 1 – Define the Base and Subclasses

```python
# Base class
class TestCase:
    def __init__(self, name):
        self.name = name
        self.status = "Not Run"

    def run(self):
        print(f"{self.name}: Running a generic test case.")
        self.status = "Passed"

# Subclass 1 – API test
class APITest(TestCase):
    def run(self):
        print(f"{self.name}: Running API test...")
        self.status = "Passed"

# Subclass 2 – UI test
class UITest(TestCase):
    def run(self):
        print(f"{self.name}: Running UI test...")
        self.status = "Passed"

# Subclass 3 – Database test
class DBTest(TestCase):
    def run(self):
        print(f"{self.name}: Running Database test...")
        self.status = "Passed"

```

## Step 2 – Use Polymorphism

- `run()` is defined in the base class but overridden in each subclass
- The `run_all_tests()` function calls `run()` without needing to know the specific object type
- Python decides which version of `run()` to call at runtime based on the actual class of the object

```python
def run_all_tests(test_list):
    for test in test_list:
        test.run()  # Each object runs its own version of run()


        # Create a list of different test types
tests = [APITest("API Test"), UITest("UI Test"), DBTest("DB Test")]

# Run them all using the shared interface
run_all_tests(tests)


```