from fastapi import FastAPI, APIRouter
import psycopg2 as psysql

from psycopg2.extras import RealDictCursor
import time

from .database import engine
from . import models
from .routers import user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)

while True:
    try: 
        conn = psysql.connect(host='localhost', database='axie-manager', user='postgres',
                       password='12345678', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Connection succesfull')
        break
    except Exception as error:
        print(f'Unable to connect.\n {error}')
        time.sleep(3)

@app.get('/')
def home():
    return {'details': 'axie manager api'}