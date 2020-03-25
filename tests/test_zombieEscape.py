from zombieEscape import create_app
import zombieEscape
import pytest
from flask import g, session


def test_import():
    assert zombieEscape


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, world!'


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.parametrize(('name', 'message'), (
    ('', b'Username is required.'),


))
def test_name(client, name, message):
    response = client.post(
        '/',
        data={'name': name}
    )
    assert message in response.data


@pytest.mark.parametrize(('name', 'location'), (
    ('bruh', 'http://localhost/start'),


))
def test_login(client, name, location):
    assert client.get('/').status_code == 200
    response = client.post(
        '/',
        data={'name': name}
    )
    assert response.headers['Location'] == 'http://localhost/game'

    with client:
        client.get('/start')
        assert session['name'] == name
