from fastapi import FastAPI
from functools import lru_cache

from api.api import api_router
from core import config

app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()

app.include_router(api_router,prefix=get_settings().api_prefix)