import pytest
from project.customers.models import Customer

@pytest.mark.parametrize("field,value", [
    ("name", "<script>alert('XSS')</script>"),
    ("city", "<b>Bold City</b>"),
    ("street", "<i>Italic Street</i>"),
    ("name", "javascript:alert('XSS')"),
    ("name", "onerror=alert('XSS')"),
])
def test_xss_vulnerability(field, value, app_context):
    """
    This test ensures that XSS payloads are either blocked (raise an exception)
    or properly sanitized before being stored.
    """
    data = {
        "name": "John Doe",
        "city": "Safe City",
        "age": 30,
        "pesel": "12345678901",
        "street": "Safe Street",
        "appNo": "A001"
    }
    data[field] = value  # Inject XSS payload into the tested field

    customer = Customer(**data)

    # XSS vulnerability test: If input is not sanitized, the test fails
    stored_value = getattr(customer, field)
    
    assert "<script>" not in stored_value, f"XSS detected in {field} (script tag found)"
    assert "javascript:" not in stored_value, f"XSS detected in {field} (javascript scheme found)"
    assert "onerror=" not in stored_value, f"XSS detected in {field} (onerror event found)"
