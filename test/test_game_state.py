import pytest

from src.card import Card
from src.deck import Deck
from src.gamestate import GameState
from src.player import Player
from src.price import VegBox

data = {
    'Price': 'Т:2 М:1 К:4 Б:0 З:3',
    'Deck': "ТТТ ТММ ТТМ МММ ТММ ТТМ",
    'Round': 1,
    'current_player_index': 1,
    'players': [
        {'name': 'Leo', 'hand': 'Т:3 М:1 К:0 Б:4 З:2', 'score': 6},
        {'name': 'Mike', 'hand': 'Т:3 М:4 К:1 Б:0 З:2', 'score': 10}]}

Leo = Player.load(data['players'][0])
Mike = Player.load(data['players'][1])
full_deck = Deck(None)
price = VegBox.load('Т:2 М:1 К:4 Б:0 З:3')


def test_init():
    players = [Leo, Mike]
    game = GameState(players=players, deck=full_deck, price=price, current_player=0, round=1)
    assert game.players == players
    assert game.deck == full_deck
    assert game.price == price
    assert game._current_player == 0
    assert game.round == 1


def test_current_players():
    players = [Leo, Mike]
    game = GameState(players=players, deck=full_deck, price=price, round=1)
    assert game._current_player == Leo
    game = GameState(players=players, deck=full_deck, price=price, current_player=1, round=1)
    assert game.current_player() == Mike


def test_eq():
    players = [Leo, Mike]
    game1 = GameState(players=players, deck=full_deck, price=price, current_player=1, round=1)
    game2 = GameState(players=players.copy(), deck=full_deck, price=price, current_player=1, round=1)
    game3 = GameState(
        players=players, deck=Deck(Card.all_cards(['Т', 'М'])), price=price, current_player=1, round=1
    )
    assert game1 == game2
    assert game1 != game3


def test_save():
    players = [Leo, Mike]
    game = GameState(players=players, deck=Deck(Card.all_cards(['Т', 'М'])), price=price, current_player=1, round=1)
    assert game.save() == data


def test_load():
    game = GameState.load(data)
    assert game.save() == data


def test_next_player():
    game = GameState.load(data)
    assert str(game.current_player()) == str(Mike)
    game.next_player()
    assert str(game.current_player()) == str(Leo)
    game.next_player()
    assert str(game.current_player()) == str(Mike)