from pydantic import BaseModel
from datetime import date
from typing import Optional

class TournamentBase(BaseModel):
    name: str
    date: date
    rule: str

class TournamentCreate(TournamentBase):
    pass

class TournamentUpdate(TournamentBase):
    name: Optional[str] = None
    date: Optional[date] = None
    rule: Optional[str] = None

class Tournament(TournamentBase):
    id: int

    class Config:
        orm_mode = True
