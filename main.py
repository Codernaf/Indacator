print("Onimisiakaami Bot is active!")

def trade_signal(direction):
    if direction == "buy":
        print("Executing strong BUY order...")
        # Place buy logic here
    elif direction == "sell":
        print("Executing strong SELL order...")
        # Place sell logic here
    else:
        print("No valid signal detected.")

# Example usage:
trade_signal("buy")
