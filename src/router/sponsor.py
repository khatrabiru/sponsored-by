from fastapi import APIRouter, Depends
from src import schemas, database
from sqlalchemy.orm import Session
from src.repository import sponsor

router = APIRouter(
    prefix="/sponsor",
    tags=['Sponsor']
)

get_db = database.get_db

@router.post('/')
def create(request: schemas.Sponsor, db: Session = Depends(get_db)):
    return sponsor.create(request, db)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return sponsor.destroy(id, db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return sponsor.update(id, request, db)


@router.get('/{id}', status_code=200)
def get(id: int, db: Session = Depends(get_db)):
    return sponsor.get(id, db)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return sponsor.get_all(db)
