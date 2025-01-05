from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
