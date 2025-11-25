import pytest
from app import app as flask_app

# The client fixture is automatically provided by pytest-flask
@pytest.fixture
def client():
    # Set the version environment variable to mock the CI environment
    flask_app.config['TESTING'] = True
    flask_app.config['APP_VERSION'] = 'test-version'
    with flask_app.test_client() as client:
        yield client

def test_root_route_ok(client):
    """Test that the root route returns a 200 OK status."""
    response = client.get('/')
    assert response.status_code == 200

def test_root_route_content(client):
    """Test that the version string is present in the response."""
    response = client.get('/')
    assert b'Application Version: test-version' in response.data

def test_health_route(client):
    """Test the dedicated health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data.decode() == 'OK'
