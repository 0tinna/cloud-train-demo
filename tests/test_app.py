from app.app import app


def test_healthz_returns_ok():
    client = app.test_client()
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "v1"}


def test_index_returns_expected_payload():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "cicd-lab", "version": "v1"}