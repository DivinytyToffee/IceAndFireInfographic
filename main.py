import json

from data_objects import CharactersCollection, BooksCollection, HousesCollection

if __name__ == '__main__':
    # characters_url = 'https://www.anapioficeandfire.com/api/characters'
    # books_url = 'https://www.anapioficeandfire.com/api/books'
    # houses_url = 'https://www.anapioficeandfire.com/api/houses'
    #
    # characters = CollectingData(characters_url)
    # books = CollectingData(books_url)
    # houses = CollectingData(houses_url)
    #
    # futures = [characters.load_data(), books.load_data(), houses.load_data()]
    #
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(futures))

    # characters = []
    books = []
    houses = []

    with open('D:\CODE\IceAndFireInfographic\char.json', 'r') as file:
        chars = json.loads(file.read())
        characters = CharactersCollection(chars)

    # for k, v in characters.storage.items():
    #     if v.father and v.mother:
    #         print(f'{v.name} - {characters.get(v.father).name} + {characters.get(v.mother).name}')

    with open('D:\CODE\IceAndFireInfographic\\book.json', 'r') as file:
        books = BooksCollection(json.loads(file.read()))

    for k, v in books.storage.items():
        print(v.name)

    with open('D:\CODE\IceAndFireInfographic\houses.json', 'r') as file:
        houses = HousesCollection(json.loads(file.read()))
        # for k, v in houses.storage.items():
        #     print(v.name)
