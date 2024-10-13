from typing import Self
from src.card import Card

class VegBox:
    VEGETABLES = ['Т', 'М', 'К', 'Б', 'З']
    MAX_PRICE = 5

    def __init__(self, **kwargs):
        self.validate_vegetables(list(kwargs.keys()))
        self.d = kwargs.copy()

    def validate_vegetables(self, symbols):
        if symbols not in self.VEGETABLES:
            raise ValueError
        #if len(self.d) != 3:
         #   raise ValueError

    def __iadd__(self, other: str | dict | Self):
        if isinstance(other, VegBox):
            other = other.d
        if isinstance(other, dict):
            other = list(other.keys())
        if isinstance(other, str):
            other = list(other)
        for v in other:
            self.d[v] = (1 + self.d.get(v, 0)) % (VegBox.MAX_PRICE + 1)
