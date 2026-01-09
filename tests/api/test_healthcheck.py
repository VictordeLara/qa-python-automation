import requests

def test_api_healthcheck():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
