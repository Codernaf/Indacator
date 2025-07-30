from telegram import Bot
import asyncio

TELEGRAM_TOKEN = "your-telegram-bot-token"
CHAT_ID = "your-chat-id"

bot = Bot(token=TELEGRAM_TOKEN)

async def send_alert(message):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"✅ Alert sent: {message}")
    except Exception as e:
        print(f"❌ Failed to send alert: {e}")

# For testing the alert function
if __name__ == "__main__":
    asyncio.run(send_alert("🚀 Test alert from your arbitrage bot!"))
