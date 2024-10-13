"""Карты Зелень"""

class Card:
    VEGETABLES = ['Т', 'М', 'К', 'Б', 'З']
    SIZE = 3

    def __init__(self, **kwargs):
        if not kwargs or sum(kwargs.values()) != self.SIZE:
            raise ValueError
        for v in self.VEGETABLES:
            setattr(self, v, kwargs[v])

    def __repr__(self):
        for v in self.VEGETABLES:
            return v * self.v

    def __eq__(self, other):
        return self.Т == other.Т and self.М == other.М \
            and self.К == other.К and self.Б == other.Б and self.З == other.З

    def score(self, price):
        return self.Т * price.Т + self.М * price.М + self.К * price.К + self.Б * price.Б + self.З * price.З

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        return Card(text.count('Т'), text.count('М'), text.count('К'), text.count('Б'), text.count('З'))

    @staticmethod
    def all_cards(VEGETABLES: list[str] | None = None):
        if VEGETABLES is None:
            VEGETABLES = Card.VEGETABLES + Card.VEGETABLES
        cards = [Card.load(veg1 * 2 + veg2 * 1) for veg1 in VEGETABLES for veg2 in VEGETABLES ]
        cards += cards.copy()
        r_card = [Card.load(veg * 3) for veg in VEGETABLES]
        for card in r_card:
            cards.remove(card)
        return cards
