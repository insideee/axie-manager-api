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
    