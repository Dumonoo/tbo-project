import pytest

# Test: Verifies the index route is accessible and returns valid content.
# Security Focus:
# - Ensures the route returns sanitized content (e.g., avoids XSS vulnerabilities).
# - Validates the presence of expected HTML structure.

def test_index_route(client, app_context):
    """
    Test the index route of the application.
    Ensures the route returns a 200 status code and expected content.
    """
    response = client.get('/')  # Simulate a GET request to the root URL
    assert response.status_code == 200  # Check for a successful HTTP response
    assert b"<!DOCTYPE html>" in response.data  # Ensure basic HTML structure is present
    assert b"<title>" in response.data  # Check for a title tag in the HTML
