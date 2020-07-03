from typing import List, Optional

from pydantic import BaseModel, EmailStr

from models.plugin import Plugin

class UserBase(BaseModel):
    username : Optional[str]
    email : Optional[EmailStr]
    is_active : Optional[bool] = True
    
class UserCreate(UserBase):
    email : EmailStr
    username : str
    password : str 

class UserUpdate(UserBase):
    password : Optional[str]

class UserInDBBase(UserBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
  #  plugins : List[Plugin] = []
  pass


class UserInDB(UserInDBBase):
    hashed_password: str


