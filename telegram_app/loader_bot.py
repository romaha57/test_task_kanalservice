from aiogram.dispatcher import Dispatcher
from aiogram import Bot

import config

bot = Bot(token=config.BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot)