from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from .. import utils
from ..database import get_db

router = APIRouter()

@router.post('/users', status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.User, db: Session=Depends(get_db)):
    
    #check unique email
    query = db.query(models.User).filter(models.User.email == user.email).first()
    if query:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='This email is already registered')
    
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    
    