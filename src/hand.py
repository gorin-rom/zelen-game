import typing

from src.card import Card


class Hand:
    def __init__(self, cards: list[Card] | None = None):
        if cards is None:
            cards = []
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def save(self) -> str:
        scards = [c.save() for c in self.cards]
        s = ' '.join(scards)
        return s

    def __eq__(self, other):
        if isinstance(other, str):
            other = Hand.load(other)
        return self.cards == other.cards

    @classmethod
    def load(cls, text: str) -> 'Hand':
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def __getattr__(self, name):
        if name in Card.VEGETABLES:
            return sum(getattr(card, name) for card in self.cards)
        raise AttributeError

    def score(self, other):
        return sum(getattr(self, v) * getattr(other, v) for v in Card.VEGETABLES)


    #   return Card.score