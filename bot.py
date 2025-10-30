import os
import logging
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)

print("=== 🚀 НАЧИНАЕМ ЗАПУСК БОТА ===")

# Токен (пока прямо в коде для теста)
BOT_TOKEN = "8072280922:AAHGvdyamtcDGYjQlGZ8_TLIW-dK-GpN9Bc"  # НЕ ЗАБУДЬТЕ ЗАМЕНИТЬ НА ВАШ ТОКЕН!
print(f"🔑 Токен получен: {'ДА' if BOT_TOKEN else 'НЕТ'}")

if not BOT_TOKEN or BOT_TOKEN == "ВАШ_ТОКЕН_ЗДЕСЬ":
    print("❌ ОШИБКА: BOT_TOKEN не найден!")
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"👋 Пользователь {update.message.from_user.first_name} запустил бота")
    await update.message.reply_text(
        f'👋 Привет, {update.message.from_user.first_name}!\n'
        '✅ Бот успешно запущен на Render! 🚀\n'
        'Все функции работают корректно!'
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"💬 Сообщение от пользователя: {update.message.text}")
    await update.message.reply_text(f'✅ Вы написали: {update.message.text}')

def main():
    try:
        print("1. 🚀 Создаем приложение бота...")
        application = Application.builder().token(BOT_TOKEN).build()
        
        print("2. 📝 Добавляем обработчики...")
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        
        print("3. ✅ Бот запускает polling...")
        print("=== 🌟 БОТ УСПЕШНО ЗАПУЩЕН ===")
        
        # Запускаем бота
        application.run_polling()
        
    except Exception as e:
        print(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
