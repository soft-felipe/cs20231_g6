from fastapi.testclient import TestClient

def test_get_home(client: TestClient) -> None:
    response = client.get("/")
    body = response.json()
    assert response.status_code == 200
    assert body == "CS-NOTESYNC: Oi, você vem sempre aqui?"