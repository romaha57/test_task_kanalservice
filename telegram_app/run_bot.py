from aiogram.utils import executor

from loader_bot import dp
from telegram_app.handlers.register_handlers import register_handlers


# функция всех хендлеров
register_handlers(dp=dp)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)