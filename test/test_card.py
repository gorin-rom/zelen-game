import pytest

from src.card import Card
from src.price import VegBox

def test_init():
    c = Card(М=2, Т=1)
    assert c.М == 2
    assert c.Т == 1
    assert c.К == 0
    assert c.Б == 0
    assert c.З == 0


def test_save():
    c = Card(Т=3)
    assert repr(c) == 'ТТТ'
    assert c.save() == 'ТТТ'
    c = Card(М=2, К=1)
    assert repr(c) == 'ММК'
    assert c.save() == 'ММК'

def test_load():
    m = 'ММК'
    c = Card.load(m)
    assert c == Card(М=2, К=1)

def test_eq():
    c1 = Card(Т=3)
    c2 = Card(Т=3)
    c3 = Card(Б=1, З=2)
    assert c1 == c2
    assert c1 != c3
    assert c2 != c3

def test_score():
    q = Card(М=2, З=1)
    p = VegBox(1, 4, 2, 3, 5)
    assert q.score(p) == 4 * 2 + 5

def test_all_cards():
    cards = Card.all_cards(['Т', 'М', 'К', 'Б', 'З'])
    expected_cards = [
        Card.load('БММ'),
        Card.load('ББК'),
        Card.load('БББ'),
        Card.load('ТТМ'),
        Card.load('ЗЗТ'),
        Card.load('ККБ')
    ]
    assert cards == expected_cards

