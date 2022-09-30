from sqlalchemy.orm import Session
from .. import models, schemas, database
from . import sponsor
from fastapi import HTTPException, status, Depends


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
    

    sponsors = request.__dict__["sponsors"]
    for item in sponsors:
        add_event(item, new_event.id, db)

    db.refresh(new_event)
    return new_event


def delete(id: int, db: Session):
    event = db.query(models.Event).filter(models.Event.id == id)

    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    sponsors = event.first().__dict__["sponsors"]
    for item in sponsors:
        delete_event(item, id, db)

    event.delete(synchronize_session=False)
    return 'done'


def update(id: int, request: schemas.Event, db: Session):
    event = db.query(models.Event).filter(models.Event.id == id)

    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    oldSponsors = event.first().__dict__["sponsors"]
    event.update(request.__dict__)
    db.commit()
    newSponsors = request.__dict__["sponsors"]

    toBeDeletedSopnsors = [x for x in oldSponsors if x not in newSponsors]
    for item in toBeDeletedSopnsors:
        delete_event(item, id, db)

    toBeAddeddSopnsors = [x for x in newSponsors if x not in oldSponsors]
    for item in toBeAddeddSopnsors:
        add_event(item, id, db)

    return 'updated'


def get(id: int, db: Session):
    event = db.query(models.Event).filter(models.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with the id {id} is not available")
    return event


def add_event(id: int, event_id: int, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id)
    if not sponsor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sponsor with id {id} not found")

    sponsors = sponsor.first().events
    sponsors.append(event_id)
    sponsor.update({"events": sponsors}, synchronize_session=False)
    db.commit()
    

def delete_event(id: int, event_id: int, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id)
    if not sponsor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sponsor with id {id} not found")

    sponsors = sponsor.first().events
    sponsors.remove(event_id)
    sponsor.update({"events": sponsors}, synchronize_session=False)
    db.commit()
