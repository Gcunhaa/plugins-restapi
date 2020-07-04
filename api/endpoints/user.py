
from fastapi import APIRouter,Depends,HTTPException, Header
from sqlalchemy.orm import Session

from typing import Any, Optional

from api import deps
from crud import crud_user
from schemas.user import UserCreate, User
from authentification.token import redis_token
from authentification.connection import redisconn
from core import security

router = APIRouter()



@router.post("/")
async def create_user(*,db : Session = Depends(deps.get_db), user_in: UserCreate) -> Any:
    """
       Criar novo usuario
    """
    user = crud_user.user.get_by_email(db,email = user_in.email)
    
    if user:
        raise HTTPException(
                status_code=400,
                detail="Já há um usuário com esse email")

    if crud_user.user.get_by_username(db,username= user_in.username):
        raise HTTPException(
                status_code=400,
                detail="Nome de usupario já em uso")

    obj = crud_user.user.create(db, obj_in= user_in)
    return obj

@router.get("/me")
async def get_user_me(*,token : str =  Depends(security.verify_token),db : Session = Depends(deps.get_db)) -> Optional[User]:
    """
       Informações usuario dono do token
    """
    user = crud_user.user.get_by_token(db=db,r=redisconn,token=token)
    return user