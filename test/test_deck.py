import pytest

from src.deck import Deck
from src.card import Card

cards = [Card.load('ТТМ'), Card.load('ММК'), Card.load('ЗЗБ'), Card.load('ЗЗЗ')]


def test_init():
    d = Deck(cards)
    assert d.cards == cards


def test_save():
    d = Deck(cards=cards)
    assert d.save() == 'ТТМ ММК БЗЗ ЗЗЗ'

    d = Deck(cards=[])
    assert d.save() == ''


def test_load():
    d = Deck.load('ТТМ ММК БЗЗ ЗЗЗ')
    expected_deck = Deck(cards)
    assert d == expected_deck


def test_draw_card():
    d1 = Deck.load('ТТМ ММК БЗЗ ЗЗЗ')
    d2 = Deck.load('ТТМ ММК БЗЗ')
    c = d1.draw_card()
    assert c == Card.load('ЗЗЗ')
    assert d1 == d2











