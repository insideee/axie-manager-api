from passlib.context import CryptContext
import requests
import ast
from .config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_account_data(ronin_address: str):
    url = f'{settings.endpoint_url}/get-update/0x{ronin_address}'

    querystring = {'id': f'0x{ronin_address}'}

    headers = ast.literal_eval(settings.header_authorization)

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data_dict = ast.literal_eval(response.text.replace('null', '"null"'))

    return data_dict