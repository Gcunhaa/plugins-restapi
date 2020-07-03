from sqlalchemy.orm import Session
 
from db import base


def init_db(db: Session) -> None:
    base.Base.metadata.create_all(db.bind)