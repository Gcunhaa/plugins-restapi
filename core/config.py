from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "GCPlugins"
    api_prefix: str = "/api/v1"

    SQLALCHEMY_DATABASE_URL: str = "postgresql://root:vertrigo123@localhost/GCPlugins"