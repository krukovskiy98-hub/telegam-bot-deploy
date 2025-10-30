import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from flask import Flask
from threading import Thread

# Настройки
BOT_TOKEN = os.environ.get('BOT_TOKEN')
PORT = int(os.environ.get('PORT', 8080))

# Flask для Railway
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Бот работает на Railway! ✅"

def run_flask():
    app.run(host='0.0.0.0', port=PORT)

# База продавцов
SELLERS = {
    "💄 Красота": [
        {
            "name": "💇 Салон 'Элит'",
            "metro": "Маяковская", 
            "address": "Москва, Тверская ул., 15",
            "rating": 4.8,
            "phone": "+7-999-123-45-67"
        }
    ]
}

async def start(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup([
        ['⚡ Наша база продавцов', '🗺️ Глобальный поиск по метро']
    ], resize_keyboard=True)
    
    await update.message.reply_text(
        f'👋 Привет, {update.message.from_user.first_name}!\n'
        'Бот успешно запущен! 🚀\n'
        'Выберите тип поиска:',
        reply_markup=keyboard
    )

async def handle_search_type(update: Update, context: CallbackContext):
    context.user_data['search_type'] = update.message.text
    categories = [['💄 Красота', '❤️ Здоровье']]
    await update.message.reply_text(
        'Выберите категорию:',
        reply_markup=ReplyKeyboardMarkup(categories, resize_keyboard=True)
    )

async def handle_category(update: Update, context: CallbackContext):
    category = update.message.text
    if category in SELLERS:
        seller = SELLERS[category][0]
        response = (
            f"🏢 {seller['name']}\n"
            f"⭐ Рейтинг: {seller['rating']}/5\n" 
            f"🚇 Метро: {seller['metro']}\n"
            f"📞 Телефон: {seller['phone']}\n"
            f"📍 Адрес: {seller['address']}"
        )
        await update
