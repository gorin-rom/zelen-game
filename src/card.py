"""Карты Зелень"""
from typing import Self

class Card:
    VEGETABLES = ['T', 'М', 'К', 'Б', 'З']
    NUMBERS = list(range(4))
    #PRICE = list(range(4))

    def __init__(self, vegs: str, vegs2: str, numb: int, numb2: int):
        if vegs not in Card.VEGETABLES:
            raise ValueError
        if numb not in Card.NUMBERS:
            raise ValueError

        self.vegs = vegs
        self.vegs2 = vegs2
        self.numb = numb
        self.numb2 = numb2

    def __repr__(self):
        if vegetable == 1:
            return f'{self.vegs}{self.numb}'
        if vegetable == 2:
            return f'{self.vegs}{self.numb}.{self.vegs2}{self.numb2}'

    def __eq__(self, other):
        if isinstance(other, str):
            other = Card.load(other)
        return self.vegs == other.vegs and self.numb == other.numb

