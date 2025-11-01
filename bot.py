import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ВРЕМЕННО - токен прямо в коде для теста
BOT_TOKEN = "8072280922:AAHGvdyamtcDGYjQlGZ8_TLIW-dK-GpN9Bc"

def start(update, context):
    update.message.reply_text("✅ Бот запущен и работает!")

def echo(update, context):
    update.message.reply_text(f"Ты сказал: {update.message.text}")

def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN не установлен!")
        return
    
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    updater.start_polling()
    logger.info("✅ Бот запущен!")
    updater.idle()

if __name__ == '__main__':
    main()
