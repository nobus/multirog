import os
import sys

path = os.getcwd()
sys.path.append(path)

from core import Game


login = "nobus"
password = "qwerty"
client = "client"


def test_add_client():
    game = Game()
    game.add_client(None)
    game.del_client(None)


def test_get_key():
    game = Game()
    k = game.get_key()
    assert len(k) == 32


def test_add_player():
    game = Game()
    resp = game.add_player(client, login)
    key = resp.get("key", False)
    assert key
    assert login == game.get_login_from_key(key)
    assert login == game.del_player(key, login)


def test_login():
    req_data = {"login": login, "password": password}
    game = Game()
    resp = game.login(client, req_data)
    key = resp.get("key", False)
    assert key
    assert resp.get("map", False) == []
    assert resp.get("players", False) == []

    req_data = {"login": login}
    resp = game.login(client, req_data)
    assert resp == "password not found"

    req_data = {"password": ""}
    resp = game.login(client, req_data)
    assert resp == "error login or password"

    req_data = {"exit": login}
    resp = game.exit_game(key, req_data)
    assert resp == login

    req_data = {"exot": login}
    resp = game.exit_game(key, req_data)
    assert resp == "error protocol"


def test_check_key():
    req_data = {"login": login, "password": password}
    game = Game()
    resp = game.login(client, req_data)
    key = resp.get("key", False)
    assert key

    req_data = {"key": key, "move": "up"}
    key2 = game.check_key(client, req_data)
    assert key == key2


def test_process_data():
    game = Game()
    resp = game.process_data(client, {})
    assert resp.get("error", "") == "please login"

    resp = game.process_data(client, {"key": ""})
    assert resp.get("error", "") == "error key"

    resp = game.process_data(client, {"login": login, "password": password})
    assert "login" in resp and type(resp["login"]) == dict


def test_notify():
    data = []
    game = Game()

    resp = game.notify(client, data)
    assert resp.get("error", "") == "need dict"
