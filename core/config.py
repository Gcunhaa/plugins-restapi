from pydantic import BaseSettings

from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "GCPlugins"
    api_prefix: str = "/api/v1"

    SQLALCHEMY_DATABASE_URL: str = "postgresql://root:vertrigo123@localhost/GCPlugins"

    REDIS_HOST: str = "redis-13113.c91.us-east-1-3.ec2.cloud.redislabs.com"
    REDIS_PASSWORD: str = "2Pw2rGli4g18YWCHST8lSmwtHq76wldb"
    REDIS_PORT: str = "13113"


@lru_cache
def get_settings():
    return Settings()