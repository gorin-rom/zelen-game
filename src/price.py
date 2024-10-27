from typing import Self
from src.card import Card


class VegBox:
    VEGETABLES = Card.VEGETABLES
    MAX_PRICE = 5

    def __init__(self, **kwargs):
        for v in self.VEGETABLES:
            setattr(self, v, kwargs.get(v))
        self.d = kwargs.copy()
        self.validate_vegetables(kwargs.keys())
        self.validate_values()

    def validate_vegetables(self, symbols):
        if symbols not in self.VEGETABLES:
            raise ValueError

    def validate_values(self, **kwargs):
        if kwargs.values() not in range(6):
            raise ValueError

    def __repr__(self):
        return ''.join(list(f'{v}:{getattr(self, v)} ' for v in self.VEGETABLES))

    def __eq__(self, other):
        for v in self.VEGETABLES:
            if getattr(self, v) != getattr(other, v):
                return False
        return True

    def add(self, other: str | dict | Self | Card):
        if isinstance(other, VegBox):
            other = other.d
        if isinstance(other, dict):
            other = list(other.keys())
        if isinstance(other, Card):
            other = list(str(other))
        if isinstance(other, str):
            other = list(other)
        for v in other:
            self.d[v] = (1 + self.d.get(v, 0)) % (VegBox.MAX_PRICE + 1)


