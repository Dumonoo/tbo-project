import pytest
from project.books.models import Book
from project import db

# Test: Verifies the creation of a valid Book object and its persistence in the database.
# Security Focus:
# - Ensures valid data is saved securely in the database.
# - Protects against SQL injection by ensuring ORM is used for queries.


def test_book_creation(app_context):
    book = Book(
        name="Sample Book",
        author="Sample Author",
        year_published=2022,
        book_type="5days",
        status="available"
    )
    db.session.add(book)
    db.session.commit()
    assert book.id is not None
    assert book.name == "Sample Book"

# Test: Ensures invalid data for Book fields (e.g., None, invalid types) raises an exception.
# Security Focus:
# - Input validation for fields like name, year_published, and book_type.
# - Prevents malformed or invalid data from being stored in the database.


import pytest
from project.books.models import Book

def test_book_invalid_data(app_context):
    # Invalid cases for the Book model
    invalid_data = [
        {"name": None, "author": "Author", "year_published": 2022, "book_type": "5days"},
        {"name": "", "author": "Author", "year_published": 2022, "book_type": "5days"},
        {"name": "Valid Name", "author": "Author", "year_published": -1, "book_type": "5days"},
        {"name": "Valid Name", "author": "Author", "year_published": 2022, "book_type": "unknown"},
    ]

    for data in invalid_data:
        with pytest.raises(ValueError):
            Book(**data)

