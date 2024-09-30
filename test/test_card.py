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
    b = 'Б3'
    c = Card.load(b)
    assert c == Card('Б', 3)
def test_eq():
    c1 = Card('Т', 3)
    c2 = Card('Т', 3)
    c3 = Card('Б', 1)
    assert c1 == c2
    assert c1 != c3
    assert c2 != c3
def test_all_cards():
    cards = Card.all_cards(['Б', 'М'], numbers=[1, 2, 3])
    expected_cards = [
        Card.load('Б1'),
        Card.load('Б2'),
        Card.load('Б3'),
        Card.load('М1'),
        Card.load('М2'),
        Card.load('М3')
    ]
    assert cards == expected_cards

    cards = Card.all_cards()
    assert len(cards) == 4 * 6
