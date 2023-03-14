from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import Resource

from loguru import logger


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1vR7Aoyj5DqYSGFaDJ4HxJ2ePKpx3Dkw46J1dUcvmBYU'


def authorization_google_api() -> Resource:
    """Авторизуемся в google api """

    logger.debug('Авторизуемся и получаем service — экземпляр доступа к API')

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    http_auth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=http_auth)

    return service


def get_data_from_sheet() -> dict:
    """Получаем данные из таблицы по spreadsheet_id"""

    service = authorization_google_api()
    logger.debug('Авторизация прошла успешно')

    # Чтение файла
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:D51',
        majorDimension='ROWS'
    ).execute()

    logger.debug('Получаем данные из Google Sheets')

    return values


if __name__ == '__main__':
    data = get_data_from_sheet()
    pprint(data)
