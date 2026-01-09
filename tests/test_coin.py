from coinflip.classes.coin import Coin


def test_coin_side_is_valid():
    coin = Coin()
    result = coin.throw_up()
    assert result in ("cara", "coroa")
