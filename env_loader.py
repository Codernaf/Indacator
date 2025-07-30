import os
from dotenv import load_dotenv

def load_env_variables():
    load_dotenv()
    env_vars = {
        "BINANCE_API_KEY": os.getenv("BINANCE_API_KEY"),
        "BINANCE_SECRET_KEY": os.getenv("BINANCE_SECRET_KEY"),
        "BYBIT_API_KEY": os.getenv("BYBIT_API_KEY"),
        "BYBIT_SECRET_KEY": os.getenv("BYBIT_SECRET_KEY"),
    }
    return env_vars
