from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# Ruta al archivo HTML fuera de cualquier subdirectorio
@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_file = Path(__file__).parent / "index.html"
    return HTMLResponse(content=index_file.read_text(), status_code=200)

# Opcional: otra ruta de prueba
@app.get("/hello", response_class=HTMLResponse)
async def say_hello():
    return "Hello, world!"
