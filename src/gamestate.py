from random import randint
from src.card import Card
from src.deck import Deck
from src.player import Player
from src.price import VegBox
import random

class GameState:
    MAX_ROUND = 6
    MIN_PLAYERS = 2
    MAX_PLAYERS = 6
    MIN_PLAYABLE_CARD = 1
    def __init__(self, players: list[Player], deck: Deck, price: VegBox, cards: list[Card], current_player: int = 0, iround: int = 1):
        self.players: list[Player] = players
        self.deck: Deck = deck
        self._current_player: int = current_player
        self.price = price
        self.cards: list[Card] = cards
        self.iround: int = iround

    def current_player(self) -> Player:
        return self.players[self._current_player]

    def __eq__(self, other):
        return (self.players == other.players and
                self.deck == other.deck and
                self._current_player == other._current_player and
                self.price == other.price and
                self.cards == other.cards and
                self.iround == other.iround)

    def save(self) -> dict:
        return {
            "Price": str(self.price),
            "Deck": str(self.deck),
            "current_player_index": self._current_player,
            "players": [p.save() for p in self.players],
            "cards": [s.save() for s in self.cards],
            "Round": self.iround
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(d) for d in data["players"]]
        return cls(
            players=players,
            deck=Deck.load(data["Deck"]),
            price=VegBox.load(data["Price"]),
            current_player=int(data["current_player_index"]),
            cards=[Card.load(s) for s in data["cards"]],
            iround=int(data["Round"])
        )

    def next_player(self):
        n = len(self.players)
        self._current_player = (self._current_player + 1) % n

    def deal_cards(self):
        num = len(self.players)
        self.cards = [self.deck.draw_card() for _ in range(num + 1)]
