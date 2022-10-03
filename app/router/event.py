from operator import ne
from fastapi import APIRouter, Depends, status
from app import database, schemas
from sqlalchemy.orm import Session
from app.repository import event, sponsor

router = APIRouter(
    prefix="/event",
    tags=['Events']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowEvent)
def create(request: schemas.Event, db: Session = Depends(get_db)):
    new_event = event.create(request, db)
    sponsors = request.__dict__["sponsors"]
    for item in sponsors:
        sponsor.add_event(item, new_event.id, db)
    return new_event


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    sponsors = event.get(id, db).sponsors
    event.delete(id, db)
    for item in sponsors:
        sponsor.delete_event(item, id, db)
    return {"message": "Event deleted."}


@router.put('/{id}')
def update(id: int, request: schemas.Event, db: Session = Depends(get_db)):

    oldSponsors = event.get(id, db).sponsors
    newSponsors = request.__dict__["sponsors"]

    event.update(id, request, db)

    toBeDeletedSopnsors = [x for x in oldSponsors if x not in newSponsors]

    for item in toBeDeletedSopnsors:
        sponsor.delete_event(item, id, db)

    toBeAddeddSopnsors = [x for x in newSponsors if x not in oldSponsors]
    for item in toBeAddeddSopnsors:
        sponsor.add_event(item, id, db)
    return {"message": "Event updated."}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id: int, db: Session = Depends(get_db)):
    return event.get(id, db)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return event.get_all(db)
