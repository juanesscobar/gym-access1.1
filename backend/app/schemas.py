# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_admin: bool
    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    name: str
    schedule: str
    capacity: int

class ClassResponse(ClassBase):
    id: int
    class Config:
        orm_mode = True
