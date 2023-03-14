import os

from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не найдены')
elif load_dotenv():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    HOST = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
else:
    exit('Переменные окружения не верные')