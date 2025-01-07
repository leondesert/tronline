import pymysql
from pymysql.cursors import DictCursor

# Конфигурация базы данных
DATABASE_CONFIG = {
    "host": "best18fv.beget.tech",
    "user": "best18fv_tron",
    "password": "QFQLTtWcy9&R",
    "database": "best18fv_tron",
    "cursorclass": DictCursor  # Возвращает результаты в виде словаря
}

# Функция для получения подключения
def get_connection():
    return pymysql.connect(**DATABASE_CONFIG)
