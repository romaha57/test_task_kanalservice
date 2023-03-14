from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

from config import HOST, PASSWORD, USER, DB_NAME

from loguru import logger


logger.debug('Подключаем к БД')
engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")

session = scoped_session(sessionmaker(bind=engine, autoflush=False))
Base = declarative_base()
