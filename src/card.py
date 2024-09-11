"""Карты Зелень"""
from typing import Self

class Card:
    VEGETABLES = ['t', 'ca', 'co', 'b', 'e']
    NUMBERS = list(range(4))

    def __init__(self, vegs: str, numb: int):
        if vegs not in Card.VEGETABLES:
            raise ValueError
        if numb not in Card.NUMBERS:
            raise ValueError

        self.vegs = vegs
        self.numb = numb

    def __repr__(self):
        if vegetable == 1:
            return f'{self.vegs}{self.numb}'
        if vegetable == 2:
            return f'{self.vegs}{self.numb}.{self.vegs}{self.numb}'



