from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from . import crud, schemas, models

app = FastAPI(title="Campus Water System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


# ================= ROOT =================
@app.get("/")
def root():
    return {"message": "Campus Water System API is running"}


# ================= DASHBOARD =================
@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={}
    )


# ================= USERS =================
@app.get("/users", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# ================= WATER ASSETS =================
@app.post("/assets", response_model=schemas.WaterAssetOut)
def create_asset(asset: schemas.WaterAssetCreate, db: Session = Depends(get_db)):
    return crud.create_water_asset(db, asset)


@app.get("/assets", response_model=list[schemas.WaterAssetOut])
def get_assets(db: Session = Depends(get_db)):
    return crud.get_water_assets(db)


# ================= INCIDENTS =================
@app.post("/incidents", response_model=schemas.IncidentOut)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    return crud.create_incident(db, incident)


@app.get("/incidents", response_model=list[schemas.IncidentOut])
def get_incidents(db: Session = Depends(get_db)):
    return crud.get_incidents(db)