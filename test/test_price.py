import pytest

from src.price import Price

def test_init():
    p = Price(2, 3, 1, 4, 0)
    assert p.Т == 2
    assert p.М == 3
    assert p.К == 1
    assert p.Б == 4
    assert p.З != 4

def test_save():
    p = Price(4, 2, 3, 1, 0)
    assert repr(p) == '42310'




