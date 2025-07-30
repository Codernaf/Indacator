import os
from dotenv import load_dotenv

def load_api_keys():
    load_dotenv()

    api_keys = {
        'binance': {
            'apiKey': os.getenv('BINANCE_API_KEY'),
            'secret': os.getenv('BINANCE_SECRET_KEY')
        },
        'bybit': {
            'apiKey': os.getenv('BYBIT_API_KEY'),
            'secret': os.getenv('BYBIT_SECRET_KEY')
        },
        # Add more exchanges here
    }
    return api_keys
