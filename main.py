import pymysql

db_config = {
    "host": "best18fv.beget.tech",
    "user": "best18fv_tron",
    "password": "QFQLTtWcy9&R",
    "database": "best18fv_tron",
}

try:
    conn = pymysql.connect(**db_config)
    print("Успешное подключение к базе данных")
    cursor = conn.cursor()
except pymysql.MySQLError as e:
    print(f"Ошибка подключения: {e}")
