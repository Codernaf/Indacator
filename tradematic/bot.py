# tradematic/bot.py

def trade_signal(direction):
    if direction == "buy":
        print("🟢 Executing strong BUY order...")
        # TODO: Connect with real buy execution logic
    elif direction == "sell":
        print("🔴 Executing strong SELL order...")
        # TODO: Connect with real sell execution logic
    else:
        print("⚪ No valid signal detected.")

# Example usage
if __name__ == "__main__":
    trade_signal("buy")
