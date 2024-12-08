import random
from typing import Self
from src.card import Card


class VegBox:
    VEGETABLES = Card.VEGETABLES
    MAX_PRICE = 5

    def __init__(self, **kwargs):
        for v in self.VEGETABLES:
            if v not in kwargs:
                setattr(self, v, random.randint(0, VegBox.MAX_PRICE))
            else:
                setattr(self, v, kwargs.get(v, 0))
        self.validate_vegetables(kwargs.keys())
        self.validate_values(kwargs.values())

    def validate_vegetables(self, symbols):
        for v in symbols:
            if v not in self.VEGETABLES:
                raise ValueError

    def validate_values(self, values):
        for v in values:
            if not 0 <= v <= VegBox.MAX_PRICE:
                raise ValueError

    def __repr__(self):
        return ' '.join(list(f'{v}:{getattr(self, v)}' for v in self.VEGETABLES))

    def __eq__(self, other):
        for v in self.VEGETABLES:
            if getattr(self, v) != getattr(other, v):
                return False
        return True

    def save(self):
        return repr(self)

    def add(self, other: str | dict | Self | Card):
        if isinstance(other, VegBox):
            other = other.VEGETABLES
        if isinstance(other, dict):
            other = list(other.keys())
        if isinstance(other, Card):
            other = list(str(other))
        for v in other:
            setattr(self, v, (getattr(self, v) + 1) % (1 + VegBox.MAX_PRICE))

    @classmethod
    def load(cls, data: str):
        """
        data format: Т:2 М:1 К:4 Б:0 З:3
        """
        items = data.split()
        params = {item.split(':')[0]: int(item.split(':')[1]) for item in items}
        return cls(**params)



