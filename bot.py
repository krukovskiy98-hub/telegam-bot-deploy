import os
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def start(update, context):
    await update.message.reply_text("✅ Бот запущен и работает!")

async def echo(update, context):
    await update.message.reply_text(f"Ты сказал: {update.message.text}")

def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN не установлен!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, echo))
    
    logger.info("✅ Бот запущен!")
    application.run_polling()

if name == '__main__':
    main()
