from fastapi.testclient import TestClient
from product_service.app import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
