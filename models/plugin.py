from sqlalchemy import Column,Boolean,String,Integer,ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Plugin(Base):
    __tablename__ = "plugins"
    
    id = Column(Integer,primary_key = True, index = True)
    name = Column(String)
    version = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"),unique = True)

    owner = relationship("User", back_populates="plugins")    
