from pydantic import BaseModel
from schemas.user import User

class Token(BaseModel):
    access_token: str
    token_type: str = "Basic"
