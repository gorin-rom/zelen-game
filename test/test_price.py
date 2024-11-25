import pytest

from src.card import Card
from src.price import VegBox


def test_init():
    p = VegBox(Т=2, М=3, К=1, Б=4, З=0)
    assert p.Т == 2
    assert p.М == 3
    assert p.К == 1
    assert p.Б == 4
    assert p.З != 4


def test_valid():
    with pytest.raises(ValueError):
        n = VegBox(Т=100)


def test_save():
    p = VegBox(Т=4, М=2, К=3, Б=1, З=0)
    assert repr(p) == 'Т:4 М:2 К:3 Б:1 З:0'


def test_add():
    v = VegBox(Т=0, М=1, К=2, Б=3, З=4)
    v.add('КББ')
    assert v.Т == 0
    assert v.М == 1
    assert v.К == 3
    assert v.Б == 5


def test_load():
    c = 'Т:4 М:0 К:3 Б:2 З:1'
    vb = VegBox.load(c)
    assert VegBox.load(c) == VegBox(Т=4, М=0, К=3, Б=2, З=1)
    assert vb.save() == c

