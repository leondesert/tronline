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
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Привет из FastAPI!"})



@app.get("/clients", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("clients.html", {"request": request, "message": "Привет из FastAPI!"})
