from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):

    employee_id: str
    full_name: str
    email: EmailStr
    department: str

class EmployeeResponse(EmployeeCreate):

    class Config:
        from_attributes = True

class EmployeeDelete(BaseModel):
    employee_id: str