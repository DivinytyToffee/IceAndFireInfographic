import asyncio
import json
import os
from enum import Enum

import aiohttp

from data_objects import CharactersCollection, BooksCollection, HousesCollection
from utils import parse_url_elem


class URLs(Enum):
    characters = 'https://www.anapioficeandfire.com/api/characters'
    books = 'https://www.anapioficeandfire.com/api/books'
    houses = 'https://www.anapioficeandfire.com/api/houses'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Collections(Enum):
    characters = CharactersCollection
    books = BooksCollection
    houses = HousesCollection

    def __repr__(self):
        return self.value


class DataLoader:

    def __init__(self, url: str, page_size: int = 10):
        self.__url = url
        self.__page_size = page_size
        self.__list_data = []

    async def __call_url(self, session: aiohttp.ClientSession, page: int):
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
        print(f'{parse_url_elem(self.__url.value, -2)} - DONE')

    @property
    def data(self):
        return self.__list_data


class Point:

    def __init__(self):
        self.__data_loaders = DataLoader
        self.__raw_data = {}
        self.__urls = URLs
        self.__collections = Collections
        self.__collections_list = []
        self.__current_dir = os.getcwd()

    def __load_from_web(self):
        for url in self.__urls:
            self.__raw_data[url.name] = self.__data_loaders(url)

        futures = [v.load_data() for k, v in self.__raw_data.items()]

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(futures))

    def __load_from_json(self):
        for collection in self.__collections:
            path = os.path.join(self.__current_dir, f'{collection.name}.json')
            with open(path, 'r') as file:
                self.__collections_list.append(collection.value(json.loads(file.read())))

    def __save_in_json(self):
        for k, v in self.__raw_data.items():
            path = os.path.join(self.__current_dir, f'{k}.json')
            with open(path, 'w') as file:
                file.write(json.dumps(v.data))
            print(f'{k} is writen in {path}')

    def __make_objects(self):
        for k, v in self.__raw_data.items():
            self.__collections_list.append(self.__collections[k].value(v.data))

    def run(self, load_from_json: bool = False):
        if load_from_json:
            self.__load_from_json()
        elif not load_from_json:
            self.__load_from_web()
            self.__save_in_json()
            self.__make_objects()

    @property
    def collections(self):
        return self.__collections_list
