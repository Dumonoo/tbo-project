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

