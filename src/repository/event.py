from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    events = db.query(models.Event).all()
    return events

def create(request: schemas.Blog,db: Session):
    new_event = models.Event(title=request.title, body=request.body,user_id=1)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def destroy(id:int,db: Session):
    event = db.query(models.Event).filter(models.Event.id == id)

    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    event.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Blog, db:Session):
    event = db.query(models.Event).filter(models.Event.id == id)

    if not event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    event.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    event = db.query(models.Event).filter(models.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with the id {id} is not available")
    return event