from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas

def get_tournament(db: Session, tournament_id: int):
    return db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()

def get_tournaments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tournament).offset(skip).limit(limit).all()

def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = models.Tournament(name=tournament.name, date=tournament.date, rule=tournament.rule)
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def update_tournament(db: Session, tournament_id: int, tournament: schemas.TournamentUpdate):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()
    if db_tournament:
        for key, value in tournament.dict(exclude_unset=True).items():
            setattr(db_tournament, key, value)
        db.commit()
        db.refresh(db_tournament)
    return db_tournament

def delete_tournament(db: Session, tournament_id: int):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()
    if db_tournament:
        db.delete(db_tournament)
        db.commit()
    return db_tournament
