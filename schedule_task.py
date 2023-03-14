import schedule

from db.services import OperationDB
from db.connection import session
from utils.log_config import run_logging

from loguru import logger

service = OperationDB(session=session)

logger.debug('Устанавливаем заполнения БД данным из Google Sheets каждый 10 сек')
schedule.every(10).seconds.do(service.fill_db)


def start_schedule():
    """Запускает отложенные задачи"""

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    run_logging()
    start_schedule()
