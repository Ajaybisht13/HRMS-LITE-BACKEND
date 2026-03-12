from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.database.database import SessionLocal
from app.models.attendance import Attendance
from app.schemas.attendance_schema import AttendanceCreate, AttendanceRequest
from app.models.employee import Employee

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add_attendance")
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(
        Employee.employee_id == data.employee_id
    ).first()

    if not employee:
        return {
            "status": 404,
            "succeeded": False,
            "message": "Employee not found",
            "data": None
        }

    existing = db.query(Attendance).filter(
        Attendance.employee_id == employee.id,
        Attendance.date == data.date
    ).first()

    if existing:
        return {
            "status": 400,
            "succeeded": False,
            "message": "Attendance already marked for this date",
            "data": None
        }

    record = Attendance(
        employee_id=employee.id,
        date=data.date,
        status=data.status
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "status": 200,
        "succeeded": True,
        "message": "Attendance marked successfully",
        "data": record
    }


@router.post("/get_attendance")
def get_attendance(data: AttendanceRequest, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(
        Employee.employee_id == data.employee_id
    ).first()

    if not employee:
        return {
            "status": 404,
            "succeeded": False,
            "message": "Employee not found",
            "data": []
        }

    records = db.query(Attendance).filter(
        Attendance.employee_id == employee.id
    ).order_by(desc(Attendance.date)).all()

    return {
        "status": 200,
        "succeeded": True,
        "message": "Attendance records fetched successfully",
        "data": records
    }