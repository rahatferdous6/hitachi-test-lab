import requests


def test_json_placeholder_posts():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data