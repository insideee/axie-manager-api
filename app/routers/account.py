from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2
from .. import utils
from ..database import get_db

router = APIRouter(prefix='/accounts',
                   tags=['Accounts'])

@router.post('/', status_code= status.HTTP_201_CREATED, response_model=schemas.AccountOut)
def create_account(account: schemas.AccountCreate, db: Session = Depends(database.get_db), 
                   user_id: int = Depends(oauth2.get_current_user)):
    
    new_account = account
    utils.get_account_data(new_account.ronin_address)
    
    return new_account