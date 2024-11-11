#class GameServer:

from src.card import Card
from src.deck import Deck
from src.player import Player
from src.price import VegBox
import random

class GameState:
    def __init__(self, players: list[Player], deck: Deck, price: VegBox, current_player: int = 0, round: int = 1):
        self.players: list[Player] = players
        self.deck: Deck = deck
        self._current_player: int = current_player
        self.price = price
        self.round = round

    def current_player(self) -> Player:
        return self.players[self._current_player]

    def __eq__(self, other):
        return (self.players == other.players and
                self.deck == other.deck and
                self._current_player == other._current_player and
                self.round == other.round)

    def save(self) -> dict:
        return {
            "price": str(self.price),
            "deck": str(self.deck),
            "current_player_index": self._current_player,
            "players": [p.save() for p in self.players],
            "round": self.round
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(d) for d in data["players"]]
        return cls(
            players=players,
            deck=Deck.load(data["deck"]),
            price=VegBox.load(data["price"]),
            current_player=int(data["current_player_index"]),
            round=int(data["round"])
        )

    def next_player(self):
        n = len(self.players)
        self._current_player = (self._current_player + 1) % n
