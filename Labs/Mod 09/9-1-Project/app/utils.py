# app/utils.py

def add(a, b):
    return a + b

def is_palindrome(s):
     # return s == s[::-1]
    return s == s[::1]

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b
