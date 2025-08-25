import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Swaasth Elder Health" in data["message"]


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_auth_endpoints_exist():
    """Test that auth endpoints are properly mounted."""
    # Test register endpoint exists (should return 422 for missing data)
    response = client.post("/api/v1/auth/register")
    assert response.status_code == 422
    
    # Test login endpoint exists (should return 422 for missing data)
    response = client.post("/api/v1/auth/login")
    assert response.status_code == 422


def test_protected_endpoints_require_auth():
    """Test that protected endpoints require authentication."""

    response = client.get("/protected-endpoint")
    assert response.status_code in [401, 403] 
    # Test users endpoint requires auth
    response = client.get("/api/v1/users/profile")
    assert response.status_code == 401
    
    # Test medicines endpoint requires auth
    response = client.get("/api/v1/medicines/")
    assert response.status_code == 401
