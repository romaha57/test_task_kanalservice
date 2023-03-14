# Тестовое задание
> Примечание
- Знаю, что файл .env, json при подключении Google API не надо загружать в git, но решил так сделать, чтобы проще проверять задание вам
- Понимаю, что выполнено не идеально, но был бы очень рад вашей конструктивной критике. Это поможет мне дальше расти как спецалист


## Задача: 
Реализовать Python скрипт

## Установка:

Google Sheet документ -  [Ссылка](https://docs.google.com/spreadsheets/d/1vR7Aoyj5DqYSGFaDJ4HxJ2ePKpx3Dkw46J1dUcvmBYU/edit#gid=0)

1. `git clone https://github.com/romaha57/test_task_kanalservice.git`
2. `pip install -r requirements.txt`


### Для запуска скрипта по получению данных и добавления в БД:
- `python schedule_task.py`

### Для запуска Flask приложения для отображения данных на странице:
- `cd flask_app`
- `python app.py`
- [Перейти в браузер](http://localhost:8000)


### Для запуска телеграм бота и отлавливания пропущенных поставок:
- `cd telegram_app`
- `python run_bot.py`
- `Перейти:` [Телеграм бот](https://t.me/ChannelServiceBot_bot)
- `В телеграм боте нажать 'start'`


## Реализованные доп.функции

- Телеграм бот по отлавливанию пропущенных поставок
- Flask страница со статистикой из БД
