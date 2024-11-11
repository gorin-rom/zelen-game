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
    t = 'ТТТ'
    z = 'ЗЗМ'
    d = Card.load(t)
    c = Card.load(m)
    q = Card.load(z)
    assert c == Card(М=2, К=1)
    assert d == Card(Т=3)
    assert q == Card(З=2, М=1)


def test_eq():
    c1 = Card(Т=3)
    c2 = Card(Т=3)
    c3 = Card(Б=1, З=2)
    c4 = Card(К=2, М=1)
    assert c1 == c2
    assert c1 != c3
    assert c2 != c3
    assert c1 != c4


def test_score():
    q = Card(М=2, З=1)
    p = VegBox(Т=1, М=4, К=2, Б=3, З=5)
    assert q.score(p) == 4 * 2 + 5


def test_all_cards():
    cards = Card.all_cards(['Т', 'М'])
    expected_cards = [
        Card.load('ТТМ'),
        Card.load('ТММ'),
        Card.load('ТТТ'),
        Card.load('ТТМ'),
        Card.load('ТММ'),
        Card.load('МММ')
    ]
    assert cards == expected_cards

