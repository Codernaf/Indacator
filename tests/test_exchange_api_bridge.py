from exchange_api_bridge import ExchangeAPIBridge

def test_fetch_price_mock():
    bridge = ExchangeAPIBridge()
    result = bridge.fetch_price("binance", "BTC/USDT")
    assert "symbol" in result or "error" in result
