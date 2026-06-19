import requests


def test_google_homepage():

    response = requests.get(
        "https://www.google.com",
        timeout=10
    )

    assert response.status_code == 200