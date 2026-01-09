from coinflip.classes.player import Player


def test_add_victory():
    p = Player("Teste")
    p.add_victory()
    assert p.consecutive_victories == 1


def test_clear_victories():
    p = Player("Teste")
    p.add_victory()
    p.clear_victories()
    assert p.consecutive_victories == 0
