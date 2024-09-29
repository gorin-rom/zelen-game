import pytest

from src.card import Card

def test_init():
    c = Card('Т', 3)
    assert c.veg == 'Т'
    assert c.number == 3

def test_save():
    c = Card('Т', 3)
    assert repr(c) == 'Т3'
    assert c.save() == 'Т3'
    c = Card('М', 2)
    assert repr(c) == 'М2'
    assert c.save() == 'М2'
def test_load():
    b = 'БББ'
    c = Card.load(b)
    assert c == Card('Б', 3)
def test_eq():
    c1 = Card('Т', 3)
    c2 = Card('Т', 3)
    c3 = Card('З', 1)
    assert c1 == c2
    assert c1 != c3
    assert c2 != c3