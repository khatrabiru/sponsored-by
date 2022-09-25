from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    sponsors = db.query(models.Sponsor).all()
    return sponsors


def create(request: schemas.Blog, db: Session):
    new_sponsor = models.Sponsor(
        title=request.title, body=request.body, user_id=1)
    db.add(new_sponsor)
    db.commit()
    db.refresh(new_sponsor)
    return new_sponsor


def destroy(id: int, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id)

    if not sponsor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event with id {id} not found")

    sponsor.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Blog, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id)

    if not sponsor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sponsor with id {id} not found")

    sponsor.update(request)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    sponsor = db.query(models.Sponsor).filter(models.Sponsor.id == id).first()
    if not sponsor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sponsor with the id {id} is not available")
    return sponsor
