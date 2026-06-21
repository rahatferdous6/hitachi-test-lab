import socket
import pytest


@pytest.mark.parametrize(
    "host,port",
    [
        ("google.com", 443),
        ("flask-container", 5000),
    ]
)
def test_tcp_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((host, port))

    sock.close()

    assert result == 0
