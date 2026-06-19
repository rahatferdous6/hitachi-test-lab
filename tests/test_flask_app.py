import requests


def test_flask_homepage():

    response = requests.get(
        "http://127.0.0.1:5000",
        timeout=5
    )

    assert response.status_code == 200

    assert "Hitachi Energy Test Lab is running!" in response.text