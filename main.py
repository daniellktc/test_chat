from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# Configura el motor de plantillas Jinja2
templates = Jinja2Templates(directory="templates")

# Ruta raíz que renderiza la plantilla index.html
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Opcional: ruta de prueba
@app.get("/hello", response_class=HTMLResponse)
async def say_hello():
    return "Hello, world!"
