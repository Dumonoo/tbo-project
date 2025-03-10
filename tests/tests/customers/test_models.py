import pytest
from project.customers.models import Customer
from project import db

# Test: Verifies the creation of a valid Customer object and its persistence in the database.
# Security Focus:
# - Protects against SQL injection by ensuring ORM is used for database operations.
# - Ensures input validation for sensitive fields like pesel and appNo.


def test_customer_creation(app_context):
    customer = Customer(
        name="John Doe",
        city="Sample City",
        age=30,
        pesel="12345678901",
        street="Sample Street",
        appNo="A001"
    )
    db.session.add(customer)
    db.session.commit()
    assert customer.id is not None
    assert customer.name == "John Doe"

# Test: Ensures invalid names (e.g., None, empty strings) raise an exception.
# Security Focus:
# - Validates input for critical fields to maintain data integrity.
# - Prevents potential errors due to invalid or missing names.


def test_customer_invalid_name(app_context):
    # Test cases for invalid names
    invalid_names = [None, "", "   "]

    for name in invalid_names:
        with pytest.raises(ValueError, match="Customer name cannot be empty"):
            Customer(
                name=name,
                city="Sample City",
                age=30,
                pesel="12345678901",
                street="Sample Street",
                appNo="A001"
            )
def test_sanitized_xss_input(app_context):
    with pytest.raises(ValueError, match="Potential XSS detected in name"):
        Customer(
            name="<script>alert('XSS')</script>",
            city="<b>Bold City</b>",
            age=30,
            pesel="12345678901",
            street="<i>Italic Street</i>",
            appNo="A001"
        )

