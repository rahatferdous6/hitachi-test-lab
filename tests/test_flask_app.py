import requests

BASE_URL = "http://flask-container:5000"


def test_flask_homepage():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
    assert "Hitachi Energy Test Lab is running!" in response.text
