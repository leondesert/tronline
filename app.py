from fastapi import FastAPI, Request, HTTPException, Form, File, UploadFile
from fastapi.responses import RedirectResponse
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import *
from settings import *

from datetime import date
import pymysql
import uuid


app = FastAPI()

# Указываем путь к папке с шаблонами
templates = Jinja2Templates(directory="templates")

# Подключаем статику (CSS, JS и т.д.)
app.mount("/static", StaticFiles(directory="static"), name="static")




# Database connection
def get_db_connection():
    return pymysql.connect(
        host='best18fv.beget.tech',
        user='best18fv_tron',
        password='QFQLTtWcy9&R',
        database='best18fv_tron',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Привет из FastAPI!"})



@app.get("/clients", response_class=HTMLResponse)
async def clients_index(request: Request):

    # clients = [
    #     {
    #         "full_name": "Olivia Rhye",
    #         "birth_year": "1994",
    #         "phone": "+77075566889",
    #         "balance": "200",
    #
    #     },
    #     {
    #         "full_name": "Olivia Rhye",
    #         "birth_year": "2014",
    #         "phone": "+77075566222",
    #         "balance": "100",
    #
    #     }
    # ]

    clients = get_clients()

    return templates.TemplateResponse("clients/index.html", {"request": request, "clients": clients})


@app.get("/clients/create", response_class=HTMLResponse)
async def clients_create(request: Request):
    return templates.TemplateResponse("clients/create.html", {"request": request})


def save_file(file: UploadFile) -> str:
    # Убедитесь, что папка для загрузок существует
    os.makedirs("uploads", exist_ok=True)

    # Генерация уникального имени файла
    ext = os.path.splitext(file.filename)[1]  # Получение расширения файла
    unique_filename = f"{uuid.uuid4()}{ext}"  # Генерация уникального имени
    filepath = os.path.join("uploads", unique_filename)

    # Сохранение файла
    try:
        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())
    except Exception as e:
        raise RuntimeError(f"Ошибка при сохранении файла: {e}")

    return filepath


def get_clients():
    try:
        # Подключение к базе данных
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # Возвращает данные в виде словарей

        # SQL-запрос для извлечения данных
        sql_query = """
        SELECT 
            id,
            full_name,
            YEAR(birth_date) as birth_date,
            phone,
            balance
        FROM clients
        """

        # Выполнение запроса
        cursor.execute(sql_query)
        results = cursor.fetchall()  # Получение всех строк результата

        print(results)

        # Закрытие курсора и соединения
        cursor.close()
        conn.close()

        return results

    except pymysql.MySQLError as e:
        print(f"Ошибка базы данных: {e}")
        return []
    except Exception as e:
        print(f"Общая ошибка: {e}")
        return []





# Маршрут для добавления клиента
@app.post("/clients/add")
async def clients_add(
    request: Request,
    full_name: str = Form(...),
    phone: str = Form(...),
    gender: str = Form(...),
    birth_date: str = Form(...),
    address: str = Form(...),
    email: str = Form(...),
    contract_number: str = Form(...),
    contract_type: str = Form(...),
    start_date: str = Form(...),
    group: str = Form(...),
    sport_rank: str = Form(...),
    photo: UploadFile = File(...),
):
    try:

        # Сохраняем фото на сервере и получаем имя файла
        photo_filename = save_file(photo)

        # Подключение к базе данных
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        # SQL запрос для вставки данных
        sql_query = """
        INSERT INTO clients (
            full_name, phone, gender, birth_date, address, email,
            contract_number, contract_type, start_date, `group`, sport_rank, photo, comment
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Выполнение запроса
        cursor.execute(sql_query, (
            full_name, phone, gender, birth_date, address, email,
            contract_number, contract_type, start_date, group, sport_rank, photo_filename, "comment"
        ))
        conn.commit()  # Фиксация изменений
        cursor.close()
        conn.close()

        # Возврат успешного ответа
        return {"status": "success", "message": "Клиент успешно добавлен"}

    except Exception as e:
        print(f"Ошибка: {e}")
        return {"status": "error", "message": e}


@app.delete("/clients/delete/{client_id}")
async def delete_client(client_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Выполняем удаление клиента
            sql = "DELETE FROM clients WHERE id = %s"
            cursor.execute(sql, (client_id,))
            connection.commit()

            # Проверяем, было ли удалено хотя бы одно совпадение
            if cursor.rowcount == 0:
                return {"status": "error", "message": "Клиент не найден"}

            return {"status": "success", "message": "Клиент удален!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        connection.close()


@app.post("/clients/delete_bulk")
async def delete_bulk_clients(request: DeleteClientsRequest):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Создаем SQL-запрос для удаления нескольких записей
            format_strings = ', '.join(['%s'] * len(request.ids))
            sql = f"DELETE FROM clients WHERE id IN ({format_strings})"
            cursor.execute(sql, tuple(request.ids))
            connection.commit()

            if cursor.rowcount == 0:
                return {"status": "error", "message": "Не найдено записей для удаления."}

            return {"status": "success", "message": "Клиенты успешно удалены"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        connection.close()



@app.get("/clients/update", response_class=HTMLResponse)
async def clients_update(request: Request):
    return templates.TemplateResponse("clients/update.html", {"request": request})



# uvicorn app:app --reload






