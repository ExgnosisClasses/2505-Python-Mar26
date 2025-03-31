# tests/test_utils.py

from app.utils import add, is_palindrome, divide
import pytest

# --- Tests for add() ---
def test_add_positive():
    assert add(3, 5) == 8

def test_add_negative():
    assert add(-4, -6) == -10

def test_add_zero():
    assert add(0, 10) == 10

# --- Tests for is_palindrome() ---
def test_palindrome_true():
    assert is_palindrome("radar") is True

def test_palindrome_false():
    assert is_palindrome("hello") is False

def test_palindrome_empty_string():
    assert is_palindrome("") is True

# --- Tests for divide() ---
def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-9, 3) == -3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
