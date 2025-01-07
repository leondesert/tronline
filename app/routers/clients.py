from fastapi import APIRouter, Request, HTTPException, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models.client import *
from app.services.client import *
from app.schemas.client import *

import uuid
import os



router = APIRouter()
templates = Jinja2Templates(directory="app/templates")



def save_file(file: UploadFile):
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




@router.get("/", response_class=HTMLResponse)
async def clients_index(request: Request):

    clients = ClientService.get_all_clients()

    return templates.TemplateResponse("clients/index.html", {"request": request, "clients": clients})



@router.get("/create", response_class=HTMLResponse)
async def clients_create(request: Request):
    client = {
        "full_name": "Андрей"
    }

    params = {
        "title_card": "Создать клиента",
        "action": "/clients/add",
    }

    return templates.TemplateResponse("clients/create.html", {
        "request": request,
        "params": params,
        "client": client
    })




# Маршрут для добавления клиента
@router.post("/add")
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
    photo: UploadFile = File(...),
):
    try:
        # Сохраняем фото на сервере и получаем имя файла
        photo_filename = save_file(photo)

        # Формируем параметры для добавления в базу данных
        client = {
            "full_name": full_name,
            "phone": phone,
            "gender": gender,
            "birth_date": birth_date,
            "address": address,
            "email": email,
            "contract_number": contract_number,
            "contract_type": contract_type,
            "start_date": start_date,
            "group": group,
            "sport_rank": sport_rank,
            "photo": photo_filename,  # Имя фото, сохраненного на сервере
            "comment": "comment"
        }


        # Добавить клиента
        ClientService.create_client(client)


        # Возврат успешного ответа
        return {"status": "success", "message": "Клиент успешно добавлен"}

    except Exception as e:
        print(f"Ошибка: {e}")
        return {"status": "error", "message": str(e)}




@router.post("/update")
async def clients_update(
    id: int = Form(...),
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

        # Формируем параметры для добавления в базу данных
        client = {
            "id": id,
            "full_name": full_name,
            "phone": phone,
            "gender": gender,
            "birth_date": birth_date,
            "address": address,
            "email": email,
            "contract_number": contract_number,
            "contract_type": contract_type,
            "start_date": start_date,
            "group": group,
            "sport_rank": sport_rank,
            "photo": photo_filename,  # Имя фото, сохраненного на сервере
            "comment": "comment"
        }

        # Добавить клиента
        message = ClientService.update_client(client)

        # Возврат успешного ответа
        return {"status": "success", "message": message}

    except Exception as e:
        print(f"Ошибка: {e}")
        return {"status": "error", "message": str(e)}




@router.delete("/delete/{client_id}")
async def delete_client(client_id: int):

    try:
        # удалить клиента
        message = ClientService.delete_client(client_id)

        return {"status": "success", "message": message}

    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.post("/delete_bulk")
async def delete_bulk(request: DeleteClientsRequest):
    try:
        # удалить клиентов
        print(request.ids)
        message = ClientService.delete_client(request.ids)

        return {"status": "success", "message": message}
    except Exception as e:
        return {"status": "error", "message": str(e)}




@router.get("/update/{client_id}", response_class=HTMLResponse)
async def clients_update(request: Request, client_id: int):

    client = ClientModel.get_client_by_id(client_id)


    params = {
        "title_card": "Редактировать клиента",
        "action": "/clients/update",
    }

    return templates.TemplateResponse("clients/create.html", {
        "request": request,
        "params": params,
        "client": client
    })

