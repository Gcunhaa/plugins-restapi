
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from typing import Any

from api import deps
from crud import crud_user
from schemas.user import UserCreate

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
                detail="Já há um usuário com esse usuário")

    obj = crud_user.user.create(db, obj_in= user_in)
    return obj