import secrets
from typing import Optional
from passlib.context import CryptContext
from redis import Redis
from fastapi import HTTPException, Header

from authentification.token import redis_token
from authentification.connection import redisconn

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

ALGORITHM = "HS256"

def verify_token(*,authorization: str )-> Optional[str]:
    token = get_token(authorization=authorization)
    if not redis_token.authorization(r=redisconn,token=token):
        raise HTTPException(status_code=401,detail={"unauthorized_client":"The authenticated client is not authorized to use this authorization grant type."})
    return token

def get_token(authorization:str):
    return authorization.split(" ")[1]

def verify_password(plain_password : str, hashed_password: str)-> bool:
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password : str)->str:
    return pwd_context.hash(password)

def generate_token()->str:
    return secrets.token_urlsafe(16)
