from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, Optional

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from redis import Redis

from authentification.token import redis_token
from core.security import verify_password,get_password_hash
from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate,UserUpdate

class CRUDUser(CRUDBase[User,UserCreate,UserUpdate]):
    def create(self, db: Session, *, obj_in: UserCreate):
        db_obj = User(
            username = obj_in.username,
            email = obj_in.email,
            password = get_password_hash(obj_in.password)
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_id(self,db: Session, *, user_id : str) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self,db: Session, *, email : str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_by_username(self,db: Session, *, username : str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def get_by_token(self,db: Session, r: Redis,*, token : str) -> Optional[User]:
        user_id = redis_token.get_user_id(str)
        if not user_id:
            return None
        return self.get_by_id(db = db,user_id = user_id)

    def authentificate(self,db:Session,*,email : str, password : str)-> Optional[User]:
        user = self.get_by_email(db,email=email)
        if not user:
            return None
        if not verify_password(password,user.password):
            return None
        return user

user = CRUDUser(User)