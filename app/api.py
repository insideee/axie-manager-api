"""Axie's api is currently private. 
The purpose of this project is to create a REST API 
for the desktop application, not find endpoints. 
That said, I'm using a third-party api."""

import aiohttp
import asyncio
from asyncio import TimeoutError
from .config import settings
import ast


async def fetch(session, headers, ronin_address, exception, params=None):
    
    try:
        if params:
            async with session.get(f'/get-update/0x{ronin_address}', headers=headers, params=params) as response:
                return await response.json()
        else:
            async with session.get(f'/get-axies/0x{ronin_address}', headers=headers) as response:
                return await response.json()
    except TimeoutError as error:
        raise exception
    
    
async def get_data(ronin_address: str, exception):
    querystring = {'id': f'0x{ronin_address}'}
    headers = ast.literal_eval(settings.header_authorization)
    timeout = aiohttp.ClientTimeout(total=5)
    
    async with aiohttp.ClientSession(base_url=settings.endpoint_url, timeout=timeout) as session:
        
        tasks = [fetch(session=session, headers=headers, params=querystring, ronin_address=ronin_address, exception=exception),
                 fetch(session=session, headers=headers, ronin_address=ronin_address, exception=exception),]
        
        return await asyncio.gather(*tasks)