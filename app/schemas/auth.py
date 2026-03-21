# app/schemas/auth.py
from pydantic import BaseModel, EmailStr
from typing import Optional

from app.models.user import UserRole


class UserRegister(BaseModel):
    name: str
    phone: str
    password: str
    role: UserRole
    email: Optional[EmailStr] = None
    momo_number: Optional[str] = None
    
class Token(BaseModel):
    access_token: str
    token_type: str