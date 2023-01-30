import json

import aiohttp


class CollectingData:

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

        print(len(self.data))

    @property
    def data(self):
        return self.__list_data