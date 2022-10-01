from fastapi import APIRouter, Depends, status
from app import database, schemas
from sqlalchemy.orm import Session
from app.repository import event

router = APIRouter(
    prefix="/event",
    tags=['Events']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Event, db: Session = Depends(get_db)):
    return event.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return event.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, request: schemas.Event, db: Session = Depends(get_db)):
    return event.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id: int, db: Session = Depends(get_db)):
    return event.get(id, db)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return event.get_all(db)
