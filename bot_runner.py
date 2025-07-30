from opportunity_detector import ArbitrageDetector
from realtime_scanner import RealTimeScanner

# Sample structure for exchange API keys
api_keys = {
    'binance': {
        'apiKey': 'your_binance_api_key',
        'secret': 'your_binance_secret_key'
    },
    'bybit': {
        'apiKey': 'your_bybit_api_key',
        'secret': 'your_bybit_secret_key'
    },
    # Add more exchanges as needed
}

# Define symbols you want to monitor
symbols = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']

# Instantiate detector and scanner
detector = ArbitrageDetector(api_keys)
scanner = RealTimeScanner(detector, api_keys, symbols, interval=3, profit_threshold=0.015)

# Run the bot
if __name__ == "__main__":
    scanner.run()
