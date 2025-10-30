import os
import logging
import sys
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)

print("=== 🚀 НАЧИНАЕМ ЗАПУСК БОТА ===")

# Токен (пока прямо в коде для теста)
BOT_TOKEN = "8072280922:AAHGvdyamtcDGYjQlGZ8_TLIW-dK-GpN9Bc"  # ЗАМЕНИТЕ НА ВАШ ТОКЕН!
print(f"🔑 Токен получен: {'ДА' if BOT_TOKEN else 'НЕТ'}")

if not BOT_TOKEN or BOT_TOKEN == "ВАШ_ТОКЕН_ЗДЕСЬ":
    print("❌ ОШИБКА: BOT_TOKEN не найден!")
    sys.exit(1)

def start(update: Update, context: CallbackContext):
    print(f"👋 Пользователь {update.message.from_user.first_name} запустил бота")
    update.message.reply_text(
        f'👋 Привет, {update.message.from_user.first_name}!\n'
        '✅ Бот успешно запущен на Render! 🚀\n'
        'Все функции работают корректно!'
    )

def echo(update: Update, context: CallbackContext):
    print(f"💬 Сообщение от пользователя: {update.message.text}")
    update.message.reply_text(f'✅ Вы написали: {update.message.text}')

def main():
    try:
        print("1. 🚀 Создаем Updater...")
        updater = Updater(BOT_TOKEN, use_context=True)
        
        print("2. 📝 Получаем dispatcher...")
        dp = updater.dispatcher
        
        print("3. 🔧 Добавляем обработчики...")
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        
        print("4. ✅ Запускаем polling...")
        print("=== 🌟 БОТ УСПЕШНО ЗАПУЩЕН ===")
        
        # Запускаем бота
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        print(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
