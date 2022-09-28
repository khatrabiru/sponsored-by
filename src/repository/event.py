from sqlalchemy.orm import Session
from .. import models, schemas
from . import sponsor
from fastapi import HTTPException, status


def get_all(db: Session):
    events = db.query(models.Event).all()
    return events


def create(request: schemas.Event, db: Session):
    new_event = models.Event(
        name=request.name,
        image_url=request.image_url,
        description=request.description,
        short_description=request.short_description,
        organized_by=request.organized_by,
        location=request.location,
        category=request.category,
        date=request.date,
        sponsors=request.sponsors)

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    sponsors = request.__dict__["sponsors"]
    for item in sponsors:
        sponsor.add_event(item, new_event.id, db)

    return "created"


def delete(id: int, db: Session):
    event = db.query(models.Event).filter(models.Event.id == id)

    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    sponsors = event.first().__dict__["sponsors"]
    for item in sponsors:
        sponsor.delete_event(item, id, db)

    event.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Event, db: Session):
    event = db.query(models.Event).filter(models.Event.id == id)

    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    oldSponsors = event.first().__dict__["sponsors"]
    newSponsors = request.__dict__["sponsors"]

    toBeDeletedSopnsors = [x for x in oldSponsors if x not in newSponsors]
    toBeAddeddSopnsors = [x for x in newSponsors if x not in oldSponsors]

    event.update(request.__dict__)
    db.commit()
    return 'updated'


def get(id: int, db: Session):
    event = db.query(models.Event).filter(models.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with the id {id} is not available")
    return event
