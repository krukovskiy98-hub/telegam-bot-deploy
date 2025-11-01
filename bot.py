import os
import logging
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ВРЕМЕННО - токен в коде для теста
BOT_TOKEN = "8072280922:AAHGvdyamtcDGYjQlGZ8_TLIW-dK-GpN9Bc"

async def start(update, context):
    await update.message.reply_text("✅ Бот запущен и работает!")

async def echo(update, context):
    await update.message.reply_text(f"Эхо: {update.message.text}")

def main():
    if not BOT_TOKEN or BOT_TOKEN == "ВАШ_ТОКЕН_ЗДЕСЬ":
        logging.error("❌ BOT_TOKEN не установлен!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    logging.info("✅ Бот запускается...")
    application.run_polling()

if __name__ == '__main__':
    main()
