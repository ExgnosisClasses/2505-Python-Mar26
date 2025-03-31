
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