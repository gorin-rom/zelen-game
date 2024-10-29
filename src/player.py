import json
import typing

from src.hand import Hand


class Player:
    def __init__(self, name: str, hand: Hand, score: int = 0):
        self.name = name
        self.hand = hand
        self.score = score

    def __str__(self):
        return f'{self.name}({self.score}): {self.hand}'

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': str(self.hand),
            'score': self.score
        }

    @classmethod
    def load(cls, data: dict):
        return cls(name=data['name'], hand=Hand.load(data['hand']), score=int(data['score']))