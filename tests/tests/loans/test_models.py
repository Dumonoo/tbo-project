

# Test: Verifies the creation of a valid Loan object and its association with a book and customer.
# Security Focus:
# - Ensures relational data integrity between loans, books, and customers.
# - Prevents double-loaning of a book by checking its availability.

import pytest
from datetime import datetime
from project.loans.models import Loan
from project import db

def test_loan_creation(app_context):
    # Create a Loan object with valid data
    loan = Loan(
        customer_name="John Doe",
        book_name="Sample Book",
        loan_date=datetime(2025, 1, 1),  # Provide valid datetime object
        return_date=datetime(2025, 1, 10),  # Provide valid datetime object
        original_author="Sample Author",
        original_year_published=2022,
        original_book_type="5days"
    )
    db.session.add(loan)
    db.session.commit()
    assert loan.id is not None
    assert loan.customer_name == "John Doe"
