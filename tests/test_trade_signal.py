from tradematic.bot import trade_signal

def test_trade_signal_valid_buy(capfd):
    trade_signal("buy")
    out, _ = capfd.readouterr()
    assert "BUY" in out

def test_trade_signal_valid_sell(capfd):
    trade_signal("sell")
    out, _ = capfd.readouterr()
    assert "SELL" in out

def test_trade_signal_invalid(capfd):
    trade_signal("hold")
    out, _ = capfd.readouterr()
    assert "No valid signal" in out
