from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)

    employee_id = Column(String, unique=True, index=True)

    full_name = Column(String)

    email = Column(String, unique=True)

    department = Column(String)

    attendance = relationship(
        "Attendance",
        cascade="all, delete",
        passive_deletes=True
    )