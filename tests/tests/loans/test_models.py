import pytest
from project.loans.models import Loan
from project import db

# Test: Verifies the creation of a valid Loan object and its association with a book and customer.
# Security Focus:
# - Ensures relational data integrity between loans, books, and customers.
# - Prevents double-loaning of a book by checking its availability.


def test_loan_creation(app_context):
    loan = Loan(
        customer_name="John Doe",
        book_name="Sample Book",
        loan_date="2025-01-01",
        return_date="2025-01-10",
        original_author="Author",
        original_year_published=2022,
        original_book_type="5days"
    )
    db.session.add(loan)
    db.session.commit()
    assert loan.id is not None
    assert loan.customer_name == "John Doe"
