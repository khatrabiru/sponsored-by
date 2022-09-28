from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    sponsors = db.query(models.Sponsor).all()
    return sponsors


def create(request: schemas.Sponsor, db: Session):
    new_sponsor = models.Sponsor(
        name=request.name,
        image_url=request.image_url,
        description=request.description,
        short_description=request.short_description,
        headquarter_location=request.headquarter_location,
        website_url=request.website_url,
        facebook_url=request.facebook_url,
        twitter_url=request.twitter_url,
        instagram_url=request.instagram_url,
        events=request.events)
    db.add(new_sponsor)
    db.commit()
    db.refresh(new_sponsor)
    return new_sponsor


def delete(id: int, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id)

    if not sponsor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    sponsor.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Sponsor, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id)

    if not sponsor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sponsor with id {id} not found")

    sponsor.update(request.__dict__)
    db.commit()
    return 'updated'


def get(id: int, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id).first()
    if not sponsor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sponsor with the id {id} is not available")
    return sponsor


def add_event(id: int, event_id: int, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id)
    if not sponsor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sponsor with id {id} not found")

    sponsors = sponsor.first().events
    sponsors.append(event_id)
    sponsor.update({"events": sponsors})
    db.commit()


def delete_event(id: int, event_id: int, db: Session):
    pass
