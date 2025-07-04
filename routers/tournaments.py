from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import schemas
from ..database import get_db

router = APIRouter()

@router.post("/tournaments/", response_model=schemas.Tournament)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db=db, tournament=tournament)

@router.get("/tournaments/", response_model=list[schemas.Tournament])
def read_tournaments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tournaments = crud.get_tournaments(db, skip=skip, limit=limit)
    return tournaments

@router.get("/tournaments/{tournament_id}", response_model=schemas.Tournament)
def read_tournament(tournament_id: int, db: Session = Depends(get_db)):
    db_tournament = crud.get_tournament(db, tournament_id=tournament_id)
    if db_tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return db_tournament

@router.put("/tournaments/{tournament_id}", response_model=schemas.Tournament)
def update_tournament(tournament_id: int, tournament: schemas.TournamentUpdate, db: Session = Depends(get_db)):
    db_tournament = crud.update_tournament(db=db, tournament_id=tournament_id, tournament=tournament)
    if db_tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return db_tournament

@router.delete("/tournaments/{tournament_id}", response_model=schemas.Tournament)
def delete_tournament(tournament_id: int, db: Session = Depends(get_db)):
    db_tournament = crud.delete_tournament(db=db, tournament_id=tournament_id)
    if db_tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return db_tournament
