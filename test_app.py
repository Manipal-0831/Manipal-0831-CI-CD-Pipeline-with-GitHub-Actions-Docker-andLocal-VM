import pytest
import os
from app import app as flask_app

@pytest.fixture
# We use the monkeypatch fixture to manipulate environment variables safely
def client(monkeypatch):
    """
    Sets the APP_VERSION environment variable for testing purposes
    and provides a Flask test client.
    """
    # Use monkeypatch to set the environment variable, which is now read dynamically in app.py's route
    monkeypatch.setitem(os.environ, 'APP_VERSION', 'test-version')
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client
    
    # Cleanup: remove the environment variable after the test runs
    # This ensures other tests aren't polluted by this environment change.
    monkeypatch.delitem(os.environ, 'APP_VERSION', raising=False)


def test_root_route_ok(client):
    """Test that the root route returns a 200 OK status."""
    response = client.get('/')
    assert response.status_code == 200

def test_root_route_content(client):
    """Test that the correct test version string is present in the response."""
    response = client.get('/')
    # This assertion now passes because the 'client' fixture correctly set the necessary environment variable.
    assert b'Application Version: test-version' in response.data

def test_health_route(client):
    """Test the dedicated health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data.decode() == 'OK'
