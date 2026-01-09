from coinflip.utils import opposite_side


def test_opposite_side():
    assert opposite_side("cara") == "coroa"
    assert opposite_side("coroa") == "cara"
