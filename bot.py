from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")  # Add BOT_TOKEN in Render env vars

async def start(update, context):
    await update.message.reply_text("Onimisiakaami Bot is active!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
