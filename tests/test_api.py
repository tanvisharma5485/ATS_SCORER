
from fastapi.testclient import TestClient
from backend.main import app


def test_health_endpoint():
    app.state.nlp = None
    app.state.embedder = None

    client = TestClient(app)
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["nlp_loaded"] is False
    assert data["embedder_loaded"] is False


def test_root_endpoint():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "ATS Resume Analyzer API"
