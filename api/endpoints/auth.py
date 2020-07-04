from fastapi import APIRouter, HTTPException, Depends, Body, Header
from typing import Optional, Any
from sqlalchemy.orm import Session
from pydantic import EmailStr

from core import security
from crud import crud_user
from api import deps
from authentification.token import redis_token
from authentification import connection
from schemas.token import Token

router = APIRouter()

@router.post("/", status_code=201)
async def auth_login(*,db : Session = Depends(deps.get_db) ,email : EmailStr = Body(...), password: str= Body(...)) -> Optional[Token]:
  """
    Fazer login
  """
  user = crud_user.user.authentificate(db,email=email,password=password)
  
  if user == None:
    raise HTTPException(status_code=401,headers={"WWW-Authentification" : "Token"})
  
  token = security.generate_token()
  r = connection.redisconn
  return redis_token.log_in(r=r,user_id=user.id,token=token)

@router.delete("/", status_code=201) 
async def auth_logout(*, token : str =  Depends(security.verify_token))-> Any:
    """[summary]
        Fazer logout
    """
    r = connection.redisconn
    redis_token.log_out(r=r,token=token)

    return "Logout realizado com sucesso"