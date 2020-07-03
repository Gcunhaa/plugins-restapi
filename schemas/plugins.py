from typing import List, Optional

from pydantic import BaseModel, EmailStr

class PluginBase(BaseModel):
    name : str
    description  : Optional[str] = None
    version : str

class PluginCreate(PluginBase):
    pass

class Plugin(PluginBase):
    id : str
    owner_id : str

    class Config():
        orm_mode = True