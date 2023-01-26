import asyncio
import json

import requests
import aiohttp


class CollectingData:

    def __init__(self, url, page_size: int = 10):
        self.__url = url
        self.__page_size = page_size
        self.__list_data = []

        # self.__characters_url = 'https://www.anapioficeandfire.com/api/characters'
        # self.__books_url = 'https://www.anapioficeandfire.com/api/books'
        # self.__houses_url = 'https://www.anapioficeandfire.com/api/houses'

    async def __call_url(self, session):
        async with session.get(self.__url) as response:
            text = await response.text()

        data = json.loads(text)
        return data

    async def load_data(self):
        async with aiohttp.ClientSession() as session:
            page = 0
            while True:
                page += 1
                response_data = await self.__call_url(session)
                if len(response_data) == 0:
                    break
                self.__list_data.extend(response_data)

    @property
    def data(self):
        return self.__list_data
