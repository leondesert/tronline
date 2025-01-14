from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, HTTPException, Form, File, UploadFile
from fastapi.templating import Jinja2Templates

from app.models.schedule import *
from app.models.group import *
from app.models.client import *
from app.services.schedule import *
from app.schemas.schedule import *
import json

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):

    classes = ScheduleService.get_all_classes()
    for classdata in classes:
        coaches = json.loads(classdata['coaches'])
        names = []
        for coach in coaches:
            client = ClientModel.get_client_by_id(coach)
            names.append(client['full_name'])

        classdata['coaches'] = ', '.join(names)
        

        group_data = GroupModel.get_group_by_id(classdata['group_id'])
        classdata['group_id'] = group_data['name']

    return templates.TemplateResponse("schedule/index.html", {"request": request, "classes": classes})



@router.get("/create", response_class=HTMLResponse)
async def create(request: Request):
    client = {
        "full_name": "Андрей"
    }

    params = {
        "title_card": "Создать занятие",
        "action": "/schedule/add",
    }

    groups = GroupModel.get_all_groups()
    clients = ClientModel.get_all_clients()
    print(clients)
    return templates.TemplateResponse("schedule/create.html", {
        "request": request,
        "params": params,
        "groups": groups,
        "clients": clients,
        "client": client
    })



@router.post("/add")
async def add(request: Request):
    try:
        form = await request.form()  # Получаем все данные из формы
        data = {}

        # Перебираем все ключи формы
        for key, value in form.items():

            data[key] = value

        # Добавить в бд
        ScheduleService.add_classes(data)

        # Возврат успешного ответа
        return {"status": "success", "message": "Занятие создано", "data": data}

    except Exception as e:
        print(f"Ошибка: {e}")
        return {"status": "error", "message": str(e)}



@router.delete("/delete/{class_id}")
async def delete(class_id: int):
    try:
        # удалить клиента
        message = ScheduleService.delete_class(class_id)

        return {"status": "success", "message": message}

    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.post("/delete_bulk")
async def delete_bulk(request: DeleteClasses):
    try:
        # удалить клиентов
        message = ScheduleService.delete_selects(request.ids)

        return {"status": "success", "message": message}
    except Exception as e:
        return {"status": "error", "message": str(e)}
