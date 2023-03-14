import datetime
import time

from aiogram import types

from db.connection import session
from db.services import OperationDB

from loguru import logger


service = OperationDB(session=session)


async def get_start(message: types.Message) -> None:
    """Обработчик команды /start и /help"""

    message_text = 'Вас приветствует бот компании <b>Каналсервис</b>\n'
    await message.answer(message_text)
    logger.debug('Запустили бота')

    while True:
        time.sleep(5)
        service.check_delivery_date()
        missed_deliveries = service.get_missed_delivery()
        if missed_deliveries:
            answer = ''
            for missed_delivery in missed_deliveries:
                answer += f'Доставка № {missed_delivery.number_order} пропущена\n'

                service.delete_missed_delivery(missed_delivery.number_order)

            await message.answer(answer)
            logger.debug('Отправили пропущенные доставки в телеграм')
        else:
            logger.debug('Пропущенных доставок не обнаружено')
