import pytest
import requests
from unittest.mock import MagicMock


@pytest.fixture

def mock_responde():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"massage": "Success"}
    return mock

def test_api_call_with_mock1(mock_responde):
    response = mock_responde
    assert response.status_code == 200
    assert response.json() == {"massage": "Success"}

def test_api_call_with_mock2(mock_responde):
    response = mock_responde
    assert response.status_code == 200
    assert response.json() == {"massage": "Success"}