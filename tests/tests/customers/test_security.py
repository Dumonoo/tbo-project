import pytest
from project.customers.models import Customer

# Test: Simulates SQL injection attempts and ensures the app does not execute malicious payloads.
# Security Focus:
# - Protects the database from SQL injection attacks.
# - Validates that all user inputs are sanitized or parameterized before being processed.


@pytest.fixture
def base_customer_data():
    return {
        "name": "Valid Name",
        "city": "Valid City",
        "age": 25,
        "pesel": "12345678901",
        "street": "Valid Street",
        "appNo": "A001"
    }

@pytest.mark.parametrize("field, payload", [
    ("name", "John'; DROP TABLE customers; --"),
    ("city", "<script>alert('XSS')</script>"),
    ("street", "' OR 1=1 --"),
    ("pesel", "1234'; DROP DATABASE; --"),
])
def test_security_injection(field, payload, base_customer_data):
    base_customer_data[field] = payload
    with pytest.raises(Exception):
        Customer(**base_customer_data)


# Test: Ensures malicious payloads (e.g., XSS scripts) in customer data are rejected.
# Security Focus:
# - Prevents XSS vulnerabilities by verifying that inputs are sanitized.
# - Protects against SQL injection in customer-related database queries.
