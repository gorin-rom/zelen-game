import pytest

from src.deck import Deck
from src.card import Card

cards = [Card('Т', 1), Card('М', 3), Card('Б', 2)]

def test_init():
    d = Deck(cards=cards)
    assert d.cards == cards

def test_save():
    d = Deck(cards=cards)
    assert d.save() == 'Т1 М3 Б2'

    d = Deck(cards=[])
    assert d.save() == ''

def test_load():
    d = Deck.load('Т1 М3 Б2')
    expected_deck = Deck(cards)
    assert d == expected_deck

def test_draw_card():
    d1 = Deck.load('Т1 М3 Б2')
    d2 = Deck.load('Т1 М3')
    c = d1.draw_card()
    assert c == Card.load('Б2')
    assert d1 == d2











