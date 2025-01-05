from fastapi import FastAPI, Request, HTTPException, Form, UploadFile
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import *
from settings import *

from datetime import date
import mysql.connector



app = FastAPI()

# Указываем путь к папке с шаблонами
templates = Jinja2Templates(directory="templates")

# Подключаем статику (CSS, JS и т.д.)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Привет из FastAPI!"})



@app.get("/clients", response_class=HTMLResponse)
async def clients_index(request: Request):

    clients = [
        {
            "full_name": "Olivia Rhye",
            "birth_year": "1994",
            "phone": "+77075566889",
            "balance": "200",

        },
        {
            "full_name": "Olivia Rhye",
            "birth_year": "2014",
            "phone": "+77075566222",
            "balance": "100",

        }
    ]

    return templates.TemplateResponse("clients/index.html", {"request": request, "clients": clients})


@app.get("/clients/create", response_class=HTMLResponse)
async def clients_create(request: Request):

    clients = [
        {
            "full_name": "Olivia Rhye",
            "birth_year": "1994",
            "phone": "+77075566889",
            "balance": "200",

        },
        {
            "full_name": "Olivia Rhye",
            "birth_year": "2014",
            "phone": "+77075566222",
            "balance": "100",

        }
    ]

    return templates.TemplateResponse("clients/create.html", {"request": request, "clients": clients})




# Маршрут для добавления клиента
@app.post("/clients/add")
async def clients_add(
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
    photo: str = Form(...),
):
    try:

        full_name = "sdasdasdas"
        phone = "23213213213"
        gender = "23213213213"
        birth_date = "06.01.2025"
        address = "23213213213"
        email = "23213213213"
        contract_number = "23213213213"
        contract_type = "23213213213"
        start_date = "06.01.2025"
        group = "23213213213"
        sport_rank = "23213213213"
        photo = "23213213213"
        comment = "23213213213"


        # Подключение к базе данных
        conn = mysql.connector.connect(**db_config)
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
            full_name, phone, gender, birth_date,
            address, email, contract_number,
            contract_type, start_date, group,
            sport_rank, photo, comment
        ))
        conn.commit()

        # Закрытие соединения
        cursor.close()
        conn.close()

        return {"message": "Клиент успешно добавлен"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Ошибка базы данных: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Неизвестная ошибка: {e}")



@app.get("/clients/update", response_class=HTMLResponse)
async def clients_update(request: Request):

    clients = [
        {
            "full_name": "Olivia Rhye",
            "birth_year": "1994",
            "phone": "+77075566889",
            "balance": "200",

        },
        {
            "full_name": "Olivia Rhye",
            "birth_year": "2014",
            "phone": "+77075566222",
            "balance": "100",

        }
    ]

    return templates.TemplateResponse("clients/update.html", {"request": request, "clients": clients})




