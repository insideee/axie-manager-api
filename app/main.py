from fastapi import FastAPI, APIRouter
from fastapi.param_functions import Depends
import psycopg2 as psysql

from psycopg2.extras import RealDictCursor
import time

from .database import engine
from .config import settings
from . import models
from .routers import user, auth, account

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(account.router)
app.include_router(auth.router)

while True:
    try: 
        conn = psysql.connect(host=settings.database_hostname, database=settings.database_name, user=settings.database_username,
                       password=settings.database_password, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Connection succesfull')
        break
    except Exception as error:
        print(f'Unable to connect.\n {error}')
        time.sleep(3)

@app.get('/')
def home():
    
    return {'details': 'axie manager api'}