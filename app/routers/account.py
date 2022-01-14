from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2
from .. import utils, api
from ..database import get_db
import time

router = APIRouter(prefix='/account',
                   tags=['Account'])

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.AccountCreatedOut)
async def create_account(account: schemas.AccountCreate, db: Session = Depends(database.get_db),
                   user: int = Depends(oauth2.get_current_user)):
    
    if account.ronin_address.find('ronin:') >= 0:
        account.ronin_address = account.ronin_address[6:]
    
    #check unique ronin account
    query = db.query(models.Account).filter(models.Account.ronin_address == account.ronin_address).first()
    if query:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='This ronin address is already registered')
    
    exception = HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='Api unavailable at the moment, Try again later.')
    data = await api.get_data(account.ronin_address, exception=exception)
    
    #check valid account
    try:
        if data[0]['leaderboard']['name'] == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid ronin address')
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid ronin address')

    new_account = models.Account(ronin_address=account.ronin_address, player_name=account.player_name, slp_total=data[0]['slp']['total'],
                                 slp_yesterday=data[0]['slp']['yesterdaySLP'], slp_today=data[0]['slp']['todaySoFar'],
                                 winrate=data[0]['leaderboard']['winRate'], average=data[0]['slp']['average'], elo=data[0]['leaderboard']['elo'],
                                 scholar_earns_percent=account.scholar_earns_percent, owner_id=user.id)
    
    total_axies = data[1]['data']['axies']['total']
    new_axies = [new_account.axies.append(models.Axie(market_id = data[1]['data']['axies']['results'][i]['id'],
                             name = data[1]['data']['axies']['results'][i]['name'],
                             stage = data[1]['data']['axies']['results'][i]['stage'],
                             class_ = data[1]['data']['axies']['results'][i]['class'],
                             breedCount = data[1]['data']['axies']['results'][i]['breedCount'],
                             image = data[1]['data']['axies']['results'][i]['image'],
                             banned = data[1]['data']['axies']['results'][i]['battleInfo']['banned'],
                             parts = data[1]['data']['axies']['results'][i]['parts'])) for i in range(total_axies)]

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account


@router.get('/{id}', response_model=schemas.AccountOut)
def get_account_by_id(id: int, db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)): 
    account = db.query(models.Account).filter(models.Account.id == id and models.Account.owner_id == user.id).first()
    
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Account with id {id} doesnt exist in the database.')
    
    return account


@router.get('/', response_model=List[schemas.AccountOut])
def get_all_accounts(db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)): 
    return user.account
