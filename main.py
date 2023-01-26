import asyncio
import json

from pathlib import Path

import requests
import aiohttp



class CollectingData:

    def __init__(self, url, page_size: int = 10):
        self.__url = url
        self.__page_size = page_size
        self.__list_data = []

    async def __call_url(self, session, page):
        url = f'{self.__url}?pageSize={self.__page_size}&page={page}'
        async with session.get(url) as response:
            print(f'Response for {url}')
            text = await response.text()

        data = json.loads(text)
        return data

    async def load_data(self):
        async with aiohttp.ClientSession() as session:
            page = 0
            while True:
                page += 1
                print(f'Page number {page}')
                response_data = await self.__call_url(session, page=page)
                if len(response_data) == 0:
                    break
                self.__list_data.extend(response_data)

        print(len(self.data))

    @property
    def data(self):
        return self.__list_data


class Characters:
    pass


class Houses:
    pass


class Books:
    pass


if __name__ == '__main__':

    characters_url = 'https://www.anapioficeandfire.com/api/characters'
    books_url = 'https://www.anapioficeandfire.com/api/books'
    houses_url = 'https://www.anapioficeandfire.com/api/houses'

    characters = CollectingData(characters_url)
    books = CollectingData(books_url)
    houses = CollectingData(houses_url)

    futures = [characters.load_data(), books.load_data(), houses.load_data()]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))


    with open('D:\CODE\IceAndFireInfographic\char.txt', 'w') as file:
        file.write(json.dumps(characters.data))

    with open('D:\CODE\IceAndFireInfographic\\book.txt', 'w') as file:
        file.write(json.dumps(books.data))

    with open('D:\CODE\IceAndFireInfographic\houses.txt', 'w') as file:
        file.write(json.dumps(houses.data))




