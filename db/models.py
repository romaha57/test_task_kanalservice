from sqlalchemy import Column, Integer, String, Date

from db.connection import Base, engine

from loguru import logger


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    number_order = Column(String, unique=True)
    price_dollar = Column(String)
    price_rub = Column(String)
    delivery_date = Column(Date)


class MissedDelivery(Base):
    __tablename__ = 'missed_deliveries'

    id = Column(Integer, primary_key=True)
    number_order = Column(String, unique=True)


logger.debug('Создаем таблицу в БД')
Base.metadata.create_all(engine)

