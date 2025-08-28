from sqlalchemy.orm import Session
from .models import User, Class

# Import dentro de la función para evitar circular import
def get_db():
    from .init_db import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ejemplos de CRUD
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_classes(db: Session):
    return db.query(Class).all()
