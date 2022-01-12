from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    avatar: str = 'default'
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    avatar: str
    
    class Config:
        orm_mode = True
                
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: int
    
class AccountCreate(BaseModel):
    ronin_address: str
    player_name: str
    scholar_earns_percent: str
    
class AccountCreatedOut(BaseModel):
    ronin_address: str
    player_name: str
    
    class Config:
        orm_mode = True
        
class AccountOut(BaseModel):
    ronin_address: str
    player_name: str
    slp_total:int
    slp_yesterday: int
    slp_today: int
    winrate: int
    average: int
    elo: int
    scholar_earns_percent: int
    
    class Config:
        orm_mode = True