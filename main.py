from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from app.routers import clients, groups
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Подключаем маршруты
app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(groups.router, prefix="/groups", tags=["Groups"])



@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})






# uvicorn app:app --reload






