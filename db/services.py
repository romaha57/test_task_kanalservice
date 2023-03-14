import datetime

from db.models import Record, MissedDelivery
from google_api.google_sheet_api import get_data_from_sheet

from db.get_dollar_currency_value import get_dollars_value

from loguru import logger


class OperationDB:
    def __init__(self, session):
        """Создаем экземпляр сессии для работы с БД"""

        self.session = session

    def get_all_records(self):
        """Получаем все записи из БД"""

        logger.debug('Получаем все записи из БД')
        records = self.session.query(Record).order_by('id').all()

        return records

    def get_missed_delivery(self):
        """Получаем все пропущенные доставки из БД"""

        logger.debug('Получаем все пропущенные доставки из БД')
        missed_delivery = self.session.query(MissedDelivery).all()

        return missed_delivery

    def delete_missed_delivery(self, number_order):
        """Удаляем пропущенную доставку из БД после уведомления в телеграм"""

        self.session.query(MissedDelivery).filter(MissedDelivery.number_order==number_order).delete()
        self.session.query(Record).filter(Record.number_order==number_order).delete()
        logger.debug('Пропущенная доставка удалена из БД')

    def check_delivery_date(self):
        """Получаем список доставок, у которых дата поставки уже пропущена и добавляем их в БД"""

        records = self.get_all_records()
        now = datetime.date.today()

        for record in records:
            if record.delivery_date > now:
                r = MissedDelivery(
                    number_order=record.number_order,
                )
                self.session.add(r)
        self.session.commit()
        logger.debug(f'Пропущенные доставки добавлены в БД')

    def _check_deleted_record(self):
        """Проверка на удаленные записи из таблицы"""

        number_order_from_db = {record.number_order for record in self.session.query(Record).all()}
        number_order_from_sheet = {record[1] for record in self.data['values'][1:]}
        self.deleted_records = number_order_from_db.difference(number_order_from_sheet)

        if self.deleted_records:
            logger.debug(f'Удаленных записей из Google Sheets {len(self.deleted_records)}')
            return True

        logger.debug('Удаленных записей из Google Sheets не обнаружено')
        return False

    def fill_db(self):
        """Добавляем данные из google sheets в БД"""

        self.data = get_data_from_sheet()
        dollar_value = get_dollars_value()

        # Удаляем все записи из БД, которые были удалены из google sheets
        if self._check_deleted_record():
            logger.debug('Удаляем записи из БД')
            for record in self.deleted_records:
                self.session.query(Record).filter(Record.number_order==record).delete()
                self.session.commit()

        for record in self.data['values'][1:]:
            number_order = record[1]
            price_dollar = record[2]
            price_rub = round(float(record[2]) * float(dollar_value), 2)
            delivery_date = record[3]

            record_from_db = self.session.query(Record).filter(Record.number_order==number_order).first()

            # если запись есть в БД, то обновляем данные
            if record_from_db:
                record_from_db.price_dollar = price_dollar
                record_from_db.price_rub = price_rub
                record_from_db.delivery_date = delivery_date
                self.session.commit()
            else:
                # добавляем новую запись
                r = Record(
                    number_order=number_order,
                    price_dollar=price_dollar,
                    price_rub=price_rub,
                    delivery_date=delivery_date
                )
                self.session.add(r)
        self.session.commit()
