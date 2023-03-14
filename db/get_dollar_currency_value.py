import datetime
from http import HTTPStatus
from xml.etree import ElementTree

import requests
from fake_useragent import UserAgent

from loguru import logger


CODE_DOLLARS_CURRENCY = 'R01235'

rand_user_agent = UserAgent().random
params = {
    'User-Agent': rand_user_agent,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}


def get_request(url: str) -> str | bool:
    """GET запрос для получения данных о курсе валют"""

    response = requests.get(url, params=params)

    if response.status_code == HTTPStatus.OK:
        logger.debug('Курс валют получен успешно')
        return response.text

    logger.warning('Произошла ошибка получения курса валют с ЦБ РФ')
    return False


def get_xml_file() -> None:
    """Получаем xml и сохраняем в файл"""

    now = datetime.date.today().strftime('%d/%m/%Y')
    url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={now}'
    response = get_request(url=url)
    if response:
        logger.debug('Записываем файл с крусами валют')
        with open('cbr.xml', 'w') as file:
            file.write(response)


def get_dollars_value() -> str:
    """Получаем значения валюты для доллара по его ID"""

    get_xml_file()

    logger.debug('Парсим XML с курсами валют и получаем значения для доллара')
    tree = ElementTree.parse('cbr.xml')
    root = tree.getroot()
    dollar = root.find(f"Valute[@ID='{CODE_DOLLARS_CURRENCY}']")
    value_dollar = dollar.find('Value').text
    value_dollar = value_dollar.replace(',', '.')

    logger.debug('Значения для доллара успешно получены')
    return value_dollar

