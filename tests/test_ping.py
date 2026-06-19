import subprocess
import pytest


@pytest.mark.parametrize("host", [
    "127.0.0.1",
    "8.8.8.8",
    "google.com"
])
def test_ping(host):
    result = subprocess.run(
        ["ping", "-c", "4", host],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0