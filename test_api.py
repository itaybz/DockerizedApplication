# test_api.py
import requests

flask = "127.0.0.1:5000/"
message = "The quick brown fox jumps over the lazy dog"
reversed_message = " ".join(message.split()[::-1])


def test_reverse_endpoint():
    url = flask + "reverse"
    params = {"in": message}
    response = requests.get(url, params=params)
    print(response)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == reversed_message


def test_restore_endpoint():
    url = flask + "restore"
    response = requests.get(url)
    assert response.status_code == 200
    result = response.json()["result"]
    assert result == reversed_message
