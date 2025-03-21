import pytest
from starlette.testclient import TestClient

@pytest.mark.v1
@pytest.mark.status
class TestStatus:
    def test_get_status(self, client: TestClient):
        response = client.get('/api/v1/status')
        assert response.status_code == 200 and len(response.json()) > 0
