"""Карты Зелень"""
class Card:
    VEGETABLES = ['Т', 'М', 'К', 'Б', 'З']
    SIZE = 3

    def __init__(self, **kwargs):
        if not kwargs or sum(kwargs.values()) != self.SIZE:
            raise ValueError
        for v in self.VEGETABLES:
            setattr(self, v, kwargs.get(v,0))

    def __repr__(self):
        return ''.join(v * getattr(self, v) for v in self.VEGETABLES)

    def __eq__(self, other):
        for v in self.VEGETABLES:
            if getattr(self, v) != getattr(other, v):
                return False
        return True
    def score(self, price):
        total = 0
        for v in self.VEGETABLES:
            total += getattr(self, v) * getattr(price, v)
        return total

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        d = {v: text.count(v) for v in Card.VEGETABLES}
        return Card(**d)

    @staticmethod
    def all_cards(VEGETABLES: list[str] | None):
        if VEGETABLES is None:
            VEGETABLES = Card.VEGETABLES
        cards = [Card.load(veg1 * 2 + veg2 * 1) for veg1 in VEGETABLES for veg2 in VEGETABLES]
        cards += cards.copy()
        r_card = [Card.load(veg * 3) for veg in VEGETABLES]
        for card in r_card:
            cards.remove(card)
        return cards
