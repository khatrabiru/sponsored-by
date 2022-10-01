from fastapi import APIRouter, Depends, status
from app import schemas, database
from sqlalchemy.orm import Session
from app.repository import sponsor

router = APIRouter(
    prefix="/sponsor",
    tags=['Sponsor']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Sponsor, db: Session = Depends(get_db)):
    return sponsor.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return sponsor.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, request: schemas.Sponsor, db: Session = Depends(get_db)):
    return sponsor.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id: int, db: Session = Depends(get_db)):
    return sponsor.get(id, db)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return sponsor.get_all(db)