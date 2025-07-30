import ccxt
import requests

def fetch_coin_price(symbol, exchange_name='binance'):
    exchange_class = getattr(ccxt, exchange_name, None)
    if not exchange_class:
        raise ValueError(f"Exchange '{exchange_name}' not supported.")
    
    exchange = exchange_class()
    ticker = exchange.fetch_ticker(symbol)
    return {
        'symbol': symbol,
        'price': ticker['last'],
        'exchange': exchange_name
    }

def fetch_price_from_coingecko(symbol_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol_id}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[symbol_id]['usd'] if symbol_id in data else None
