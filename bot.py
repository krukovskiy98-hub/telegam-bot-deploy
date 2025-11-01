import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("✅ Бот запущен и работает!")

def echo(update, context):
    update.message.reply_text(f"Ты сказал: {update.message.text}")

def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN не установлен!")
        return
    
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    updater.start_polling()
    logger.info("✅ Бот запущен!")
    updater.idle()

if name == '__main__':
    main()
