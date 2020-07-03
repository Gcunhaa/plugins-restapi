from fastapi import APIRouter, HTTPException, Depends
from typing import Optional, Any
from sqlalchemy.orm import Session

from core import security
from crud import crud_user
from api import deps

router = APIRouter()

@router.post("/")
async def auth_login(*,db : Session = Depends(deps.get_db),email : str, password: str) -> Any:
    user = crud_user.user.authentificate(db,email=email,password=password)
    if user == None:
      raise HTTPException(status_code=401,detail="Email ou senha incorreto")
    return "foi"

@router.delete("/")
async def auth_logout():
    return "teste"