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
    
class AccountOut(BaseModel):
    ronin_address: str
    player_name: str