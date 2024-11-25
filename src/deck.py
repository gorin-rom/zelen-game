import random
import typing

from src.card import Card


class Deck:
    def __init__(self, cards: None | list[Card]):
        if cards is None:
            cards = Card.all_cards(None)
            random.shuffle(cards)
        self.cards: list[Card] = cards

    def __eq__(self, other):
        if isinstance(other, str):
            other = Deck.load(other)
        return self.cards == other.cards

    def __repr__(self):
        return self.save()

    def save(self) -> str:
        scards = [c.save() for c in self.cards]
        s = ' '.join(scards)
        return s

    @classmethod
    def load(cls, text: str) -> typing.Self:
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def draw_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

