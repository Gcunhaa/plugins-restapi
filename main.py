from fastapi import FastAPI
import uvicorn

from api.api import api_router
from core import config

app = FastAPI()

app.include_router(api_router,prefix=config.get_settings().api_prefix)


