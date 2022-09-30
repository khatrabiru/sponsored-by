from fastapi import APIRouter, Depends
from app import schemas, database
from sqlalchemy.orm import Session
from app.repository import sponsor

router = APIRouter(
    prefix="/sponsor",
    tags=['Sponsor']
)

get_db = database.get_db


@router.post('/')
def create(request: schemas.Sponsor, db: Session = Depends(get_db)):
    return sponsor.create(request, db)


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return sponsor.delete(id, db)


@router.put('/{id}')
def update(id: int, request: schemas.Sponsor, db: Session = Depends(get_db)):
    return sponsor.update(id, request, db)


@router.get('/{id}', status_code=200)
def get(id: int, db: Session = Depends(get_db)):
    return sponsor.get(id, db)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return sponsor.get_all(db)


@router.get('/details/{id}', status_code=200)
def get_sponsor_detail(id: int, db: Session = Depends(get_db)):
    # TODO(Find basic details of evenyts and attached to Json)
    return sponsor.get(id, db)
