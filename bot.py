import os
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8072280922:AAHGvdyamtcDGYjQlGZ8_TLIW-dK-GpN9Bc"

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

if __name__ == '__main__':
    main()
