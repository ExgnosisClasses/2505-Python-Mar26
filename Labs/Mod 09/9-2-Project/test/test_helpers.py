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
