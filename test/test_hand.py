import pytest

from src.card import Card
from src.hand import Hand
from src.price import VegBox


cards = [Card.load('БЗЗ'), Card.load('ТКК'), Card.load('МММ')]


def test_init():
    d = Hand(cards)
    assert d.cards == cards


def test_save():
    h = Hand(cards=cards)
    assert h.save() == 'БЗЗ ТКК МММ'


def test_load():
    d = Hand.load('БЗЗ ТКК МММ')
    exp_deck = Hand(cards)
    assert d == exp_deck


def test_add_card():
    h = Hand.load('БЗЗ ТКК МММ')
    h.add_card(Card.load('ТТТ'))
    assert repr(h) == 'БЗЗ ТКК МММ ТТТ'

    h.add_card(Card.load('БББ'))
    assert repr(h) != 'БЗЗ ТКК МММ ТТТ ББК'
    assert repr(h) == 'БЗЗ ТКК МММ ТТТ БББ'

def test_score():
    h = Hand(cards=[Card.load('ТББ')])
    p = VegBox(Т=1, М=5, К=3, Б=2, З=4)
    assert h.score(p) == 1 + 2 * 2

















