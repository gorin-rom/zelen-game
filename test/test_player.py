from src.hand import Hand
from src.player import Player

def test_init():
    h = Hand.load('ТТТ ТЗЗ БММ')
    p = Player(name='Leo', hand=h, score=15)
    assert p.name == 'Leo'
    assert p.hand == h
    assert p.score == 15

def test_load():
    d = {'hand': 'ТТТ ТЗЗ БММ', 'name': 'Leo', 'score': 15}
    h_exp = Hand.load('ТТТ ТЗЗ БММ')
    p_exp = Player(name='Leo', hand=h_exp, score=15)
    assert str(p_exp) == str(Player.load(d))

def test_save():
    h = Hand.load('ТТТ ТЗЗ БММ')
    p = Player(name='Leo', hand=h, score=15)
    assert str(p) == 'Leo(15): ТТТ ТЗЗ ММБ'
    assert p.save() == {'hand': 'ТТТ ТЗЗ ММБ', 'name': 'Leo', 'score': 15}