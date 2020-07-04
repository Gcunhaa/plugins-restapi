from typing import Any,Optional
from redis import Redis

from schemas.token import Token

class REDISToken():
    def log_in(self,r: Redis,*,user_id:str, token: str) -> Optional[Token]:
        if not r.set(token,user_id):
            return None

        return Token(access_token = token)

    def log_out(self,r: Redis, *, token: str) -> bool:
        return r.delete(token)

    def authorization(self, r: Redis, *, token: Token) -> bool:
        return r.exists(token)

    def get_user_id(self,r: Redis,*,token : str) -> Optional[str]:
        return r.get(token)
    

redis_token = REDISToken()