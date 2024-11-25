import pytest

from src.card import Card
from src.deck import Deck
from src.gamestate import GameState
from src.player import Player
from src.price import VegBox

data = {
    "Price": 'Т:2 М:1 К:4 Б:0 З:3',
    "Deck": 'ТТМ ТММ ТТТ ТТМ ТММ МММ',
    "Round": 1,
    "current_player_index": 1,
    "cards": ['ЗЗЗ', 'БЗЗ', 'ББЗ'],
    "players": [
        {'name': 'Leo', 'hand': 'ТТТ МММ ТММ', 'score': 6},
        {'name': 'Mike', 'hand': 'ТТМ ТММ ТТМ', 'score': 10}]}

Leo = Player.load(data["players"][0])
Mike = Player.load(data["players"][1])
cards = (Card.load(s) for s in data["cards"])
full_deck = Deck(None)
price = VegBox.load('Т:2 М:1 К:4 Б:0 З:3')


def test_init():
    players = [Leo, Mike]
    game = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player=0, iround=1)
    assert game.players == players
    assert game.deck == full_deck
    assert game.price == price
    assert game.cards == cards
    assert game._current_player == 0
    assert game.iround == 1


def test_current_players():
    players = [Leo, Mike]
    game = GameState(players=players, deck=full_deck, price=price, cards=cards, iround=1)
    assert game.current_player() == Leo
    game = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player=1, iround=1)
    assert game.current_player() == Mike


def test_eq():
    players = [Leo, Mike]
    game1 = GameState(players=players, deck=full_deck, price=price, cards=cards, current_player=1, iround=1)
    game2 = GameState(players=players.copy(), deck=full_deck, price=price, cards=cards, current_player=1, iround=1)
    game3 = GameState(
        players=players, deck=Deck(Card.all_cards(['Б', 'З'])), price=price, cards=cards, current_player=1, iround=1
    )
    assert game1 == game2
    assert game1 != game3


def test_save():
    players = [Leo, Mike]
    game = GameState(players=players, deck=Deck(Card.all_cards(['Т', 'М'])), price=price, cards=cards, current_player=1, iround=1)
    assert game.save() == data


def test_load():
    game = GameState.load(data)
    assert game.save() == data


def test_next_player():
    game = GameState.load(data)
    assert str(game.current_player()) == 'Mike(10): ТТМ ТММ ТТМ'
    game.next_player()
    assert str(game.current_player()) == 'Leo(6): ТТТ МММ ТММ'
    game.next_player()
    assert str(game.current_player()) == 'Mike(10): ТТМ ТММ ТТМ'
