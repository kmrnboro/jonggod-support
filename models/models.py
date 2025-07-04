from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(Date)
    rule = Column(String)
