from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, HTTPException, Form, File, UploadFile
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/groups", response_class=HTMLResponse)
async def groups_index(request: Request):
    return templates.TemplateResponse("groups/index.html", {"request": request})
