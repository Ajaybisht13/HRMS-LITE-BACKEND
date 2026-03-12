from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeDelete

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/employees")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):

    existing = db.query(Employee).filter(
        Employee.employee_id == employee.employee_id
    ).first()

    if existing:
        return {
            "status": 400,
            "succeeded": False,
            "message": "Employee already exists",
        }

    new_employee = Employee(**employee.model_dump())

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "status": 200,
        "succeeded": True,
        "message": "Employee added successfully",
        "data": new_employee
    }


@router.get("/employees")
def get_employees(db: Session = Depends(get_db)):

    employees = db.query(Employee).all()

    if not employees:
        return {
        "status": 200,
        "succeeded": True,
        "message": "No employees found",
        "data": []
    }

    return {
        "status": 200,
        "succeeded": True,
        "message": "Employees fetched successfully",
        "data": employees
    }


@router.post("/employees/delete")
def delete_employee(data: EmployeeDelete, db: Session = Depends(get_db)):

    emp = db.query(Employee).filter(
        Employee.employee_id == data.employee_id
    ).first()

    if not emp:
        return {
            "status": 404,
            "succeeded": False,
            "message": "Employee not found",
        }

    db.delete(emp)
    db.commit()

    return {
        "status": 200,
        "succeeded": True,
        "message": "Employee deleted successfully"
    }