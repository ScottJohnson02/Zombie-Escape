import zombieEscape


def test_import():
    assert zombieEscape


def start_game():
    response = client.get('/')
    assert response.data == b'Welcome to zombie escape'
