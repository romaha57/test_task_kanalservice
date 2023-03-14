from aiogram import Dispatcher

from telegram_app.handlers.start_handler import get_start


def register_handlers(dp: Dispatcher) -> None:
    """Функция для регистрации всех хендлеров"""

    dp.register_message_handler(get_start, commands=['start', 'help'])
