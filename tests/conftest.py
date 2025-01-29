import pytest
from project import app, db


@pytest.fixture(scope="module")
def app_context():
    """
    Provides a Flask application context for tests.
    Ensures that the database schema is created and dropped after tests.
    """
    with app.app_context():
        db.create_all()  # Create the database schema
        yield  # Provide the context to the test
        db.session.remove()  # Clean up the session
        db.drop_all()  # Drop the schema


@pytest.fixture(scope="module")
def client():
    """
    Provides a test client for sending HTTP requests to the Flask application.
    """
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use an in-memory database
    app.config["WTF_CSRF_ENABLED"] = False  # Disable CSRF for easier testing

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database schema
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()  # Drop the schema after tests


@pytest.fixture
def sample_book_data():
    """
    Provides sample data for creating Book objects.
    """
    return {
        "name": "Sample Book",
        "author": "Sample Author",
        "year_published": 2022,
        "book_type": "5days",
        "status": "available",
    }


@pytest.fixture
def sample_customer_data():
    """
    Provides sample data for creating Customer objects.
    """
    return {
        "name": "John Doe",
        "city": "Sample City",
        "age": 30,
        "pesel": "12345678901",
        "street": "Sample Street",
        "appNo": "A001",
    }


@pytest.fixture
def sample_loan_data():
    """
    Provides sample data for creating Loan objects.
    """
    return {
        "customer_name": "John Doe",
        "book_name": "Sample Book",
        "loan_date": "2025-01-01",
        "return_date": "2025-01-10",
        "original_author": "Sample Author",
        "original_year_published": 2022,
        "original_book_type": "5days",
    }
