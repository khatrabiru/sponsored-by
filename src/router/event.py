from fastapi import APIRouter
from src import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.repository import event

router = APIRouter(
    prefix="/event",
    tags=['Events']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return event.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return event.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return event.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return event.show(id, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def all(id: int, db: Session = Depends(get_db)):
    return event.show(id, db)
