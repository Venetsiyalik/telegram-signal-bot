import os
import logging
import ccxt
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API tokenlar
TELEGRAM_TOKEN = os.getenv("7731519812:AAHdfhUpz1OZe44b98eleN3zl3eaB1ImsYs")
OPENAI_API_KEY = os.getenv("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")
openai.api_key = OPENAI_API_KEY

# Telegram logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Binance client
exchange = ccxt.binance()

# Signal generatsiya
async def generate_signal():
    data = exchange.fetch_ticker('ADA/USDT')
    price = data['last']
    message = f"ADA narxi: {price} USDT\nTavsiya: Hozircha kuting, bozor beqaror."
    return message

# Telegram komandalar
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Men ADA signal botman.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await generate_signal()
    await update.message.reply_text(msg)

# Bot ishga tushirish
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
