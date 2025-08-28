# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ---------------- CONFIGURACIÓN ----------------
# Cambia este URL según tu base de datos
DATABASE_URL = "sqlite:///./gym_access.db"  # SQLite local (simple para desarrollo)
# Ejemplo PostgreSQL:
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

# ---------------- MOTOR ----------------
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # solo para SQLite
)

# ---------------- SESIÓN ----------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ---------------- DEPENDENCIA FASTAPI ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# backend/database.py