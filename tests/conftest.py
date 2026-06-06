"""Pytest configuration and shared fixtures for tests."""
import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    """Fixture that provides a TestClient for the FastAPI app."""
    return TestClient(app)
