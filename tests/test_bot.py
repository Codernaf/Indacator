from bot import trade_signal  # Replace 'bot' with your real filename if different

def test_trade_signal_buy(capsys):
    trade_signal("buy")
    captured = capsys.readouterr()
    assert "🟢 Executing strong BUY order..." in captured.out

def test_trade_signal_sell(capsys):
    trade_signal("sell")
    captured = capsys.readouterr()
    assert "🔴 Executing strong SELL order..." in captured.out

def test_trade_signal_invalid(capsys):
    trade_signal("hold")
    captured = capsys.readouterr()
    assert "⚪ No valid signal detected." in captured.out
