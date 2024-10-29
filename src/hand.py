import typing

from src.card import Card


class Hand:
    def __init__(self, cards:  list[Card] | None = None):
        if cards is None:
            cards = []
        self.cards: list[Card] = cards
        '''for v in Card.VEGETABLES:
            setattr(self, v, kwargs.get(v, 0))'''

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

    def save(self) -> str:
        scards = [c.save() for c in self.cards]
        s = ' '.join(scards)
        return s

    @classmethod
    def load(cls, text: str) -> typing.Self:
        cards = [Card.load(s) for s in text.split()]
        return cls(cards=cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def score(self, other):
        return self.veg * other.veg
     #   return Card.score