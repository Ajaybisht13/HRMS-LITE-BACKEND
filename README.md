# HRMS Lite – Backend API

## Overview

This is the backend API for **HRMS Lite**, a lightweight Human Resource Management System.

The backend is built using **FastAPI** and provides RESTful APIs to manage employees and track attendance records. It connects to a **PostgreSQL database** using **SQLAlchemy ORM**.

The API is consumed by the React frontend application.

---

# Live Backend

API Base URL

https://hrms-lite-backend-rjyw.onrender.com/api/

Swagger API Documentation

https://hrms-lite-backend-rjyw.onrender.com/docs

---

# Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn
* Docker (for containerization)

---

# Features

## Employee Management

The API allows the admin to:

* Add new employees
* View employee list
* Delete employees

Employee fields:

* Employee ID (unique)
* Full Name
* Email
* Department

---

## Attendance Management

The API allows the admin to:

* Mark attendance for employees
* View attendance records by employee
* Prevent duplicate attendance entries for the same date

Attendance fields:

* Employee ID
* Date
* Status (Present / Absent)

---

# Project Structure

```id="backendstructure1"
backend
│
├── app
│   ├── database
│   │   └── database.py
│   │
│   ├── models
│   │   ├── employee.py
│   │   └── attendance.py
│   │
│   ├── routers
│   │   ├── employee_router.py
│   │   └── attendance_router.py
│   │
│   ├── schemas
│   │   ├── employee_schema.py
│   │   └── attendance_schema.py
│   │
│   └── main.py
│
├── requirements.txt
├── Dockerfile
└── .env
```

---

# Environment Variables

Create a `.env` file inside the backend directory.

Example:

```id="envexample1"
DATABASE_URL=postgresql://username:password@host:port/database
```

Example for PostgreSQL:

```id="envexample2"
DATABASE_URL=postgresql://user:password@localhost:5432/hrms
```

For production (Render PostgreSQL):

```id="envexample3"
DATABASE_URL=postgresql://username:password@host/database
```

---

# Running the Backend Locally

## 1. Navigate to backend folder

```id="runbackend1"
cd backend
```

---

## 2. Create virtual environment

```id="runbackend2"
python -m venv venv
```

---

## 3. Activate virtual environment

Mac/Linux

```id="runbackend3"
source venv/bin/activate
```

Windows

```id="runbackend4"
venv\Scripts\activate
```

---

## 4. Install dependencies

```id="runbackend5"
pip install -r requirements.txt
```

---

## 5. Run FastAPI server

```id="runbackend6"
uvicorn app.main:app --reload
```

Backend will run at

```id="runbackend7"
http://localhost:8000
```

Swagger documentation

```id="runbackend8"
http://localhost:8000/docs
```

---

# API Endpoints

## Employee APIs

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| POST   | /api/employees        | Add employee      |
| GET    | /api/employees        | Get all employees |
| POST   | /api/employees/delete | Delete employee   |

---

## Attendance APIs

| Method | Endpoint            | Description            |
| ------ | ------------------- | ---------------------- |
| POST   | /api/add_attendance | Mark attendance        |
| POST   | /api/get_attendance | Get attendance records |

---

# Database

The application uses **PostgreSQL** as the database.

Tables:

* employees
* attendance

Relationships:

* One employee can have multiple attendance records.

---

# Docker Support

Build Docker image

```id="dockerbuild"
docker build -t hrms .
```

Run container

```id="dockerrun"
docker run --env-file .env -p 8000:8000 hrms
```

---

# Deployment

Backend is deployed using **Render**.

Deployment includes:

* FastAPI API server
* PostgreSQL cloud database
* Docker container support

---

# Limitations

* No authentication implemented
* No employee update API
* No pagination for employee list
* No advanced HR modules such as payroll or leave management

---

# Author

Ajay Bisht
