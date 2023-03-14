from loguru import logger


def run_logging() -> None:
    """Запускает функцию до старта бота для начала логирования"""
    debug_log_write()
    warning_log_write()


def debug_only(record):
    """Функция для фильтрации записи в логи только для уровня DEBUG"""

    return record["level"].name == 'DEBUG'


def warning_only(record):
    """Функция для фильтрации записи в логи только для уровня WARNING"""

    return record["level"].name == 'WARNING'


def debug_log_write():
    """Записывает в debug.log служебные сообщения"""

    logger.add('logs/debug.log', format="{time} {level} {message}", level="DEBUG", rotation="50 KB",
           compression="zip", filter=debug_only)


def warning_log_write():
    """Записывает в warning.log сообщения об ошибках"""

    logger.add('logs/warning.log', format="{time} {level} {message}", level="WARNING", rotation="50 KB",
           compression="zip", filter=warning_only)