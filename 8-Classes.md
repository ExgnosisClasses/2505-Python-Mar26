# 8 - Python Classes

## Why OOP for Testers?

Test automation tools like Selenium, PyTest, Robot Framework, and test frameworks often use object-oriented (OO) structures

Understanding OOP helps testers:
- Write reusable test components
- Structure test code more clearly
- Understand the internals of automation frameworks

## Object-Oriented Programming

OOP is a programming paradigm where we model real-world entities as “objects” in code.
- Classes are used as a template to create objects
- A class definition can also be thought of a type definition and all objects created from the class definition are of that type.
- The act of creating an object from a definition is called `instantiation` and the created object is called an `instance` of the class

### Classes

Objects in the real world have three basic aspects

#### Attributes

This is the data that uniquely defines the object.
- For example, a person has the attributes of name, age and height
- Each instance in Python has the same defined attributes, but has its own set of values for those attribute
- The variables that store attributes in a class are called instance variables.
- In other words, each instance has its own copy of the class defined instance variables

#### Methods

Objects in the real world have behaviours that are characteristic of their type
- In a class, this is encoded as a class method, which is just a function that is defined inside a class
- An instance of a class will execute a method if it gets sent a message corresponding to the method
- The message can be sent by another object, a piece fo Python or from another method in the same instance

### Identity

Each instantiated object has its own unique identity, existence and lifetime
- We can often distinguish objects because they occupy different memory locations
- More commonly, we add some attribute to serve as an identifier which is a more robust and preferred way of uniquely identifying objects.

### OOP Techniques

OOP code is characterized by several basic techniques

#### Encapsulation 

Also referred to as data hiding
- The internal data of a class is not accessed directly
- Reading and writing an object's data (implementation) is done only through an object’s methods (interface)
- This allows us to change the way we keep the underlying data and ensuring that we don't break other code if we keep the interface unchanged
- In other words, we can change how the internal data is processed without changing how other objects interact with the object

#### Inheritance

In the real world, types for a hierarchy
- Dogs are mammals therefore they have all the properties of mammals
- Inheritance allows us to emulate these hierarchies in code
- For example, we create a class `mammal`
- Then we create classes `dog` and `cat`

#### Polymorphism

Since object execute a message
- The result of sending a message depends on the object that receives it
- This means the calling object sends a request for a service
- The receiving object determines how to process that request
- An example of declarative programming
- We can change functionality by changing the implementation of the receiving object
- Polymorphism, the same message can have different forms of results

#### Abstraction

Refers to dropping unnecessary parts of a class definition
- We abstract away (get rid of) whatever we don't need
- A user object on a website may represent a person, but we don't need to know their eye colour or blood pressure

--- 

##  Classes and Objects 

The Python standard class definition looks like this

```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running test case: {self.name}")

```

-`class` – defines a class. By convention, class names are capitalized
-`__init__()` – constructor, runs when an object is created
- `self` – refers to the current object instance
- `self.name` - the name attribute for the instance
- `run()` - the instance methods

Creating objects:

```python
class TestStep:
    def __init__(self, description):
        
        self.description = description
        print(f"Creating step object {self.description}")

    def execute(self):
        print(f"Executing step: {self.description}")

# Creating steps
step1 = TestStep("Open login page")
step2 = TestStep("Enter credentials")

# Using them
step1.execute()
step2.execute()

```
 And we can see the two objects created
 

```python
print(type(step1))
print(id(step1))
print(id(step2))

```

```shell
<class '__main__.TestStep'>
139675229543536
139675229545936
```

The code provided in the above example is _not_ an example of data hiding.
- The variable `descripton` can be accessed by using the notation `object.variable`
- This is called `breaking encapsulation` because once we start using objects of this type, we can't rename or change the definition of `description`

```python
class TestStep:
    def __init__(self, description):

        self.description = description
        print(f"Creating step object {self.description}")

    def execute(self):
        print(f"Executing step: {self.description}")

# Creating steps
step1 = TestStep("Open login page")

# Accessing data no encapsulation
print(f"initial value '{step1.description}'")
step1.description = "John Cleese Rocks"
print(f"modified value '{step1.description}'")
```

```shell
Creating step object Open login page
initial value 'Open login page'
modified value 'John Cleese Rocks'
```

### Encapsulation

In this example, we encapsulate the data

```python
class SecureLogin:
    def __init__(self):
        self.__password = None  # private attribute

    def set_password(self, pwd):
        if len(pwd) >= 8:
            self.__password = pwd
        else:
            print("Password too short!")

    def get_password(self):
        return "******"

login = SecureLogin()

```

`self.__password` is a private attribute (note the double underscore __). This means:
- Python will name-mangle this attribute so it can't be accessed as `object.__password` from outside.
- This protects it from accidental access or modification from other parts of the code.

```python
login = SecureLogin()
login.__password
```

```shell
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[9], line 15
     12         return "******"
     14 login = SecureLogin()
---> 15 login.__password

AttributeError: 'SecureLogin' object has no attribute '__password'
```

```python
    def set_password(self, pwd):
        if len(pwd) >= 8:
            self.__password = pwd
        else:
            print("Password too short!")

```

This is a setter method.
- it checks if the provided password pwd has at least 8 characters.
  - If yes: it stores it in the private attribute __password.
  - If not: it prints a warning and does not store it.

```python
    def get_password(self):
        return "******"

```

This is a getter method.
- Instead of returning the actual password, it returns masked output (******) to avoid exposing sensitive info.
- This implements controlled access to internal state.

Note that without a defined setter, the object's data is read only.
- In this case, the value fo the data is normally set in the `__init__` method


---

## Inheritance

Inheritance allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or superclass).

This lets you:
- Reuse code from existing classes
- Extend or customize behavior
- Avoid duplication (DRY Principle - "don't repeat yourself")

### How Inheritance Works in Python

Python allows a class to be derived from another class by putting the parent class name in parentheses:

```python
class Parent:
    # Base functionality

class Child(Parent):
    # Inherits everything from Parent

```

#### Example: Single Inheritance

```python
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Running test case: {self.name}")

class LoginTest(TestCase):  # Inherits from TestCase
    def validate(self):
        print("Validating login functionality")

# Create an object of the subclass
lt = LoginTest("Login Test 001")
lt.run()         # Inherited method
lt.validate()    # Child class method

```

- `LoginTest` inherits from `TestCase`
- `LoginTest` gets the `__init__()` and `run()` methods for free
- You can add new methods like `validate()` to extend the behavior

### Method Overriding

If the child class defines a method with the same name as one in the parent, it overrides the parent’s version.


```python
class TestCase:
    def run(self):
        print("Running base test case...")

class LoginTest(TestCase):
    def run(self):  # Overrides the parent's method
        print("Running login test...")

tc = TestCase()
tc.run()  # Output: Running base test case...

lt = LoginTest()
lt.run()  # Output: Running login test...

```

You can still call the original method using super().
- We often use this form when we want to add some functionality to the parent method in the child class.
- This avoids copying the parent method code into the child method

```python
class TestCase:
    def run(self):
        print("Running base test case...")

class LoginTest(TestCase):
    
    def run(self):
        super().run()
        print("Additional login test logic")

lt = LoginTest()
lt.run()  # Output: Running login test...
```

### Multiple Inheritance

Python supports multiple inheritance, where a class inherits from more than one parent class.

```python
class ReportGenerator:
    def generate(self):
        print("Generating test report...")

class LogHandler:
    def log(self):
        print("Logging test execution...")

class TestUtility(ReportGenerator, LogHandler):
    pass

tu = TestUtility()
tu.generate()  # From ReportGenerator
tu.log()       # From LogHandler

```

Multiple inheritance can be powerful but may lead to:
- Method name conflicts
- Complicated Method Resolution Order (MRO)
- Use it carefully, especially in test automation frameworks.

With potential conflicts where the same method is defined in more than one base class, it uses the order in which the parents are listed resolve which to use

```pythoclass LogHandler:
    def log(self):
        print("Logging test execution...")

class ReportGenerator:
    def log(self):
        print("Generating test report...")


class TestUtility(ReportGenerator, LogHandler):
    pass

tu = TestUtility()
tu.log()  # From ReportGenerator
  
```

But 

```python

class LogHandler:
    def log(self):
        print("Logging test execution...")

class ReportGenerator:
    def log(self):
        print("Generating test report...")


class TestUtility(LogHandler,ReportGenerator):
    pass

tu = TestUtility()
tu.log()  # From LogHandler
  
```

---

## Polymorphism

Polymorphism means "many forms."
- Allows objects of different classes to be treated through a common interface
- Meaning you can call the same method name (run(), execute(), etc.) on different object types, and each will respond in its own way.

##### Why Should Testers Care?

Polymorphism is highly useful in automated testing, especially when:
- You have different kinds of tests (UI, API, database) but want to run them through a common test runner.
- You want to reduce duplicate logic in your test framework.
- You need to swap test objects dynamically without rewriting code.


```python
class TestCase:
    def run(self):
        print("Running a generic test case.")

class SmokeTest(TestCase):
    def run(self):
        print("Running a quick smoke test.")

class RegressionTest(TestCase):
    def run(self):
        print("Running a full regression test.")

```

Now use polymorphism:

```python
def execute_test(test_obj):
    test_obj.run()

# Create objects of different types
smoke = SmokeTest()
regression = RegressionTest()

# Run tests through the same interface
execute_test(smoke)       # Output: Running a quick smoke test.
execute_test(regression)  # Output: Running a full regression test.
```

What’s Happening?
- SmokeTest and RegressionTest both override the run() method.
- The execute_test() function accepts any object that has a run() method — it doesn’t care about the class.
- Each object behaves differently, depending on its own class definition.


### Real-World Example

Let’s say you’re building a framework that can run different types of tests:

```python
class APITest(TestCase):
    def run(self):
        print("Running API test...")

class UITest(TestCase):
    def run(self):
        print("Running UI test...")

class DBTest(TestCase):
    def run(self):
        print("Running Database test...")

```

You can use a loop to handle them uniformly:

```python
test_suite = [APITest(), UITest(), DBTest()]

for test in test_suite:
    test.run()

```

