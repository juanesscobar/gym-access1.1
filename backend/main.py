from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Archivos estáticos
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Templates HTML
templates = Jinja2Templates(directory="frontend/templates")

# ---------- HTML ROUTES ----------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/members", response_class=HTMLResponse)
async def members(request: Request):
    return templates.TemplateResponse("members.html", {"request": request})

@app.get("/trainings", response_class=HTMLResponse)
async def trainings(request: Request):
    return templates.TemplateResponse("trainings.html", {"request": request})

@app.get("/commerce", response_class=HTMLResponse)
async def commerce(request: Request):
    return templates.TemplateResponse("commerce.html", {"request": request})

@app.get("/exercises", response_class=HTMLResponse)
async def exercises(request: Request):
    return templates.TemplateResponse("exercises.html", {"request": request})

@app.get("/qr", response_class=HTMLResponse)
async def qr(request: Request):
    return templates.TemplateResponse("qr.html", {"request": request})

# ---------- API ROUTES ----------
@app.get("/api/members")
async def get_members():
    return [
        {"id": 1, "name": "John Doe", "membership": "Premium"},
        {"id": 2, "name": "Jane Smith", "membership": "Basic"}
    ]

@app.get("/api/trainings")
async def get_trainings():
    return [
        {"id": 1, "title": "Cardio Blast", "duration": "30min"},
        {"id": 2, "title": "Strength Training", "duration": "45min"}
    ]

@app.get("/api/products")
async def get_products():
    return [
        {"id": 1, "name": "Protein Shake", "price": 5.99},
        {"id": 2, "name": "Gym Gloves", "price": 12.50}
    ]

@app.get("/api/qr")
async def get_qr():
    return {"qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAA.."}  # truncado
