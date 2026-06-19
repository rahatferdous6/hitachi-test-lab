import socket
import pytest


@pytest.mark.parametrize("host,port", [
    ("127.0.0.1", 22),
    ("127.0.0.1", 3389),
    ("google.com", 443)
])
def test_tcp_port(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((host, port))

    sock.close()

    assert result == 0