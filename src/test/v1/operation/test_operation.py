from starlette.testclient import TestClient


class TestOperation:
    def test_get_operation(self, client: TestClient):
        response = client.get('/api/v1/operation')
        print(response.json())
        assert response.status_code == 200 and len(response.json()) > 0