import pytest
import requests

@pytest.mark.parametrize("endpoint", [
    "/posts",
    "/comments",
    "/users"
])
def test_api_endpoints_healthcheck(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200
    assert response.json() is not None
