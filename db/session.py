from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import Settings

engine = create_engine(Settings().SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)