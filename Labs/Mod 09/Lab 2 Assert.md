# Lab 9-2: Writing Assertions for Real-World Testing Scenarios

---

## Setup Instructions

Directory layout:

```text
project/
├── app/                      # Application code
│   ├── __init__.py
│   └── helpers.py            # Code under test
│
└── tests/                    # Pytest test files
    ├── __init__.py
    └── test_helpers.py       # Pytest test file

```

Create the directory structure, and create the helpers.py class with the following code.

```python
def get_status_code():
    return 200

def get_user_profile():
    return {
        "username": "testuser",
        "email": "user@example.com",
        "roles": ["admin", "editor"]
    }

def parse_xml(xml_str):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_str)
    return root.find("name").text

def get_element_text():
    # Simulate UI element text
    return "Submit"
```

Create the test directory, and create the test_helpers.py file with the following code

```python
# tests/test_helpers.py

from app.helpers import (
    get_status_code,
    get_user_profile,
    parse_xml,
    get_element_text
)

# --- Assertions: Numbers and Equality ---
def test_status_code():
    assert get_status_code() == 200

# --- Assertions: Dictionaries and Membership ---
def test_user_profile_keys():
    profile = get_user_profile()
    assert "username" in profile
    assert profile["email"].endswith("@example.com")
    assert "admin" in profile["roles"]

# --- Assertions: XML Value Check ---
def test_parse_xml_name():
    xml = "<user><name>Alice</name></user>"
    assert parse_xml(xml) == "Alice"

# --- Assertions: String and Identity ---
def test_element_text():
    text = get_element_text()
    assert text == "Submit"
    assert isinstance(text, str)

# --- Assertions: Exception Handling ---
import pytest

def test_parse_invalid_xml():
    broken_xml = "<user><name></user>"  # malformed XML
    with pytest.raises(Exception):
        parse_xml(broken_xml)

```

## Run the tests

Run the following command from the project root:

```shell
(base) 9-2-project$ conda activate labs
(labs) 9-2-project$ pytest
```
You should see output similar to the following

```shell

==================================================================================================== test session starts =====================================================================================================
platform linux -- Python 3.12.9, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/rod/working/pytest/9-2-project
plugins: anyio-3.7.1
collected 5 items                                                                                                                                                                                                            

tests/test_helpers.py .....                                                                                                                                                                                            [100%]

===================================================================================================== 5 passed in 0.01s ======================================================================================================

```

## Break a Test and Debug

In test_user_profile_keys(), change:

```python
assert "admin" in profile["roles"]
```

to:

```python
assert "viewer" in profile["roles"]
```
    
Re-run pytest and you should see output like this

```shell
========================================================================================================== FAILURES ==========================================================================================================
___________________________________________________________________________________________________ test_user_profile_keys ___________________________________________________________________________________________________

    def test_user_profile_keys():
        profile = get_user_profile()
        assert "username" in profile
        assert profile["email"].endswith("@example.com")
>       assert "viewer" in profile["roles"]
E       AssertionError: assert 'viewer' in ['admin', 'editor']

tests/test_helpers.py:19: AssertionError
================================================================================================== short test summary info ===================================================================================================
FAILED tests/test_helpers.py::test_user_profile_keys - AssertionError: assert 'viewer' in ['admin', 'editor']
================================================================================================ 1 failed, 4 passed in 0.05s =================================================================================================

```
