```python
import requests

BASE_URL = "http://172.17.0.2:5000"


def test_health():
    response = requests.get(f"{BASE_URL}/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "UP"


def test_version():
    response = requests.get(f"{BASE_URL}/version")

    assert response.status_code == 200

    data = response.json()

    assert data["version"] == "1.0"


def test_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2

    assert data[0]["name"] == "Alice"

    assert data[1]["name"] == "Bob"
```
