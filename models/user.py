from sqlalchemy import Column,Boolean,String,Integer
from sqlalchemy.orm import relationship

from db.base_class import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key = True, index = True)
    username = Column(String, index = True, unique = True)
    password = Column(String)
    email = Column(String, index = True, unique = True)
    is_active = Column(Boolean, default=True)

    #plugins = relationship("Plugin", back_populates="owner")  
