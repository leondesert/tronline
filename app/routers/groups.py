from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, HTTPException, Form, File, UploadFile
from fastapi.templating import Jinja2Templates

from app.models.group import *
from app.services.group import *
from app.schemas.group import *
import json

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):

    groups = GroupModel.get_all_groups()

    return templates.TemplateResponse("groups/index.html", {"request": request, "groups": groups})



@router.get("/create", response_class=HTMLResponse)
async def create(request: Request):
    client = {
        "full_name": "Андрей"
    }

    params = {
        "title_card": "Создать группу",
        "action": "/groups/add",
    }

    return templates.TemplateResponse("groups/create.html", {
        "request": request,
        "params": params,
        "client": client
    })



@router.post("/add")
async def add(request: Request):
    try:

        form = await request.form()  # Получаем все данные из формы
        data = {}
        repeater_group = []

        # Перебираем все ключи формы
        for key, value in form.items():
            if key.startswith("repeater-group"):
                # Парсим динамическую группу
                key_parts = key.split("[")
                group_index = int(key_parts[1][:-1])  # Извлекаем индекс
                field_name = key_parts[2][:-1]  # Извлекаем имя поля
                # Добавляем в список
                while len(repeater_group) <= group_index:
                    repeater_group.append({})
                repeater_group[group_index][field_name] = value
            else:
                data[key] = value

        # Добавляем repeater_group в итоговый словарь

        json_data = json.dumps(repeater_group) # Преобразование массива в JSON
        data["schedule"] = json_data

        print(data)


        # Добавить в бд
        GroupModel.add_group(data)

        # Возврат успешного ответа
        return {"status": "success", "message": "Группа создана", "data": data}

    except Exception as e:
        print(f"Ошибка: {e}")
        return {"status": "error", "message": str(e)}



@router.delete("/delete/{group_id}")
async def delete(group_id: int):

    try:
        # удалить клиента
        message = GroupModel.delete(group_id)

        return {"status": "success", "message": message}

    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.post("/delete_bulk")
async def delete_bulk(request: DeleteGroups):
    try:
        # удалить клиентов
        message = GroupModel.delete_selects(request.ids)

        return {"status": "success", "message": message}
    except Exception as e:
        return {"status": "error", "message": str(e)}
