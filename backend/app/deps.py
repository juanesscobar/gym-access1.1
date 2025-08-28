from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .crud import get_db
from .models import User

def get_current_user(db: Session = Depends(get_db)):
    user = db.query(User).first()  # Ejemplo simple
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no autenticado"
        )
    return user

def admin_required(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos de administrador"
        )
    return current_user
