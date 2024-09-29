"""Карты Зелень"""

class Card:
    VEGETABLES = ['Т', 'М', 'К', 'Б', 'З']
    NUMBERS = list(range(1, 4))

    def __init__(self, veg: str, number: int):
        if veg not in Card.VEGETABLES:
            raise ValueError
        if number not in Card.NUMBERS:
            raise ValueError

        self.veg = veg
        self.number = number

    def __repr__(self):
        return f'{self.veg}{self.number}'

    def __eq__(self, other):
        return self.veg == other.veg and self.number == other.number

    def score(self, other):
        return self.veg * other.veg

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        return Card(veg=text[0], number=int(text[1]))
