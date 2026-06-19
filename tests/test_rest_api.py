import requests


def test_health():

    response = requests.get(
        "http://127.0.0.1:5000/health"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "UP"


def test_version():

    response = requests.get(
        "http://127.0.0.1:5000/version"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["version"] == "1.0"


def test_users():

    response = requests.get(
        "http://127.0.0.1:5000/users"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2

    assert data[0]["name"] == "Alice"

    assert data[1]["name"] == "Bob"