"""
Integration tests for API endpoints.
"""
import pytest
from fastapi.testclient import TestClient

from apps.api.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


def test_root_endpoint(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_endpoint(client):
    """Test health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_smartcar_connect(client):
    """Test Smartcar OAuth connect endpoint."""
    # TODO: implement test
    response = client.get("/auth/smartcar/connect")
    assert response.status_code in [200, 302]  # Redirect or OK


def test_get_fleet_vehicles(client):
    """Test getting fleet vehicles."""
    # TODO: implement test with auth
    pass
