from fastapi import FastAPI

from app.database.database import engine, Base
from app.routers import employee_router, attendance_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://ajaybisht13.github.io",
    "https://ajaybisht13.github.io/HRMS-LITE"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # easiest for assignment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_router.router, prefix="/api")
app.include_router(attendance_router.router, prefix="/api")