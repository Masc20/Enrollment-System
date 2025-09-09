# 🎓 Enrollment System

A modern **Enrollment System** built with **FastAPI**, **Python**, and **PostgreSQL**.  
Implements an **async REST API** for managing students, courses, and enrollment workflows.  

---

## 📌 Tech Stack

### 🔹 Back-End
- **Language**: Python 3.11+  
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) – async REST API framework  
- **Database**: PostgreSQL  
- **ORM**: [SQLAlchemy 2.0+ (async)](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)  
- **DB Driver**: [asyncpg](https://github.com/MagicStack/asyncpg)  
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)  
- **Environment management**: [python-dotenv](https://pypi.org/project/python-dotenv/)  
- **Testing**: [pytest](https://docs.pytest.org/en/stable/)  
- **Validation & Serialization**: [Pydantic](https://docs.pydantic.dev/)  
- **API Docs**: Auto-generated via FastAPI (Swagger UI, ReDoc)  

### 🔹 Front-End (Undecided yet...)
- **Framework**: (React, Vue, Angular, or your choice)  
- **UI Library**: (Bootstrap, Tailwind, etc.)  
- **State Management**: (Redux, Pinia, Zustand, etc.)  
- **API Communication**: Axios / Fetch API  

---
## 📂 Project Structure

The project follows a modular and scalable architecture, separating concerns between backend logic, API layers, data models, and configuration. Below is the directory structure:
   
enrollment-system/ ├── backend/ │ ├── app/ │ │ ├── main.py # FastAPI application entry point │ │ ├── api/ # API route definitions (v1, etc.) │ │ ├── models/ # SQLAlchemy ORM models │ │ ├── schemas/ # Pydantic models for request/response validation │ │ ├── services/ # Business logic and data processing │ │ ├── db.py # Async database connection setup (using SQLAlchemy + asyncpg/psycopg) │ │ └── config.py # Configuration and environment variable management │ ├── alembic/ # Database migration scripts (via Alembic) │ ├── tests/ # Unit and integration tests │ └── requirements.txt # Python dependencies for the backend │ ├── frontend/ # Placeholder for future front-end implementation (e.g., React/Vue) │ └── README.md # Project documentation
---

## ⚡ Installation & Setup

### 1. Clone the repo
```bash```
git clone https://github.com/Masc/enrollment-system.git
cd enrollment-system

### 2. Backend Setup
Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Example requirements.txt
fastapi
uvicorn[standard]
sqlalchemy>=2.0
asyncpg
alembic
pydantic
python-dotenv
pytest

## Run server
uvicorn app.main:app --reload


## API will be available at:
👉 http://127.0.0.1:8000/docs (Swagger UI)
👉 http://127.0.0.1:8000/redoc (ReDoc)

### 3. Database Setup

Make sure you have PostgreSQL installed and running.

Create a database:

CREATE DATABASE enrollment_db;


Apply migrations:

alembic upgrade head

### 4. Front-End Setup

🚧 To be decided (React/Vue/Angular/etc.)
open for suggestions

🧪 Testing

Run tests with:

pytest






