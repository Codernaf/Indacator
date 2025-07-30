import ccxt
import time
from user_config import exchange, symbol, amount

def execute_trade():
    try:
        orderbook = exchange.fetch_order_book(symbol)
        bid = orderbook['bids'][0][0]
        ask = orderbook['asks'][0][0]
        spread = ask - bid

        print(f"Best Bid: {bid}, Best Ask: {ask}, Spread: {spread}")

        if spread > 1:  # You can adjust this threshold
            # Place a buy order
            print(f"Placing buy order for {amount} {symbol} at {ask}")
            buy_order = exchange.create_market_buy_order(symbol, amount)
            print("Buy order executed:", buy_order)

            time.sleep(2)  # Wait for the market

            # Place a sell order
            print(f"Placing sell order for {amount} {symbol} at {bid}")
            sell_order = exchange.create_market_sell_order(symbol, amount)
            print("Sell order executed:", sell_order)

        else:
            print("Spread too small. No trade executed.")

    except Exception as e:
        print("Trade execution failed:", str(e))

# Run the trade
execute_trade()
