from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.database.database import engine, Base
from app.routers import employee_router, attendance_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HRMS Lite API",
    description="Backend API for HRMS Lite project",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "https://ajaybisht13.github.io",
    "https://ajaybisht13.github.io/HRMS-LITE"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

app.include_router(employee_router.router, prefix="/api", tags=["Employees"])
app.include_router(attendance_router.router, prefix="/api", tags=["Attendance"])