"""Unit tests for FastAPI application endpoints."""
import pytest


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_read_root_status_code(self, client):
        """Test that root endpoint returns 200 status code."""
        response = client.get("/")
        assert response.status_code == 200

    def test_read_root_response_structure(self, client):
        """Test that root endpoint returns expected JSON structure."""
        response = client.get("/")
        data = response.json()
        assert "message" in data
        assert "status" in data

    def test_read_root_response_values(self, client):
        """Test that root endpoint returns correct message values."""
        response = client.get("/")
        data = response.json()
        assert data["message"] == "Hello from FastAPI!"
        assert data["status"] == "running"

    def test_read_root_content_type(self, client):
        """Test that root endpoint returns JSON content type."""
        response = client.get("/")
        assert response.headers["content-type"] == "application/json"


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_check_status_code(self, client):
        """Test that health endpoint returns 200 status code."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_check_response_structure(self, client):
        """Test that health endpoint returns expected JSON structure."""
        response = client.get("/health")
        data = response.json()
        assert "status" in data

    def test_health_check_response_value(self, client):
        """Test that health endpoint returns healthy status."""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"

    def test_health_check_content_type(self, client):
        """Test that health endpoint returns JSON content type."""
        response = client.get("/health")
        assert response.headers["content-type"] == "application/json"
