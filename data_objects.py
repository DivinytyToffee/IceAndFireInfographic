from utils import parse_url_elem


class BaseObject:
    _links_list: list

    def __init__(self, data: dict):
        self.__data = data
        self.__parse()
        self.__split_links()

    def __repr__(self):
        char = self.__class__.__name__
        return f"{char} - {self.__dict__.get('name', char)}"

    def __parse(self):
        self.__dict__.update(self.__data)

    def __split_links(self):
        for link_name in self._links_list:
            if self.__dict__[link_name]:
                if isinstance(self.__dict__[link_name], list):
                    self.__dict__.update({link_name: list(int(parse_url_elem(x)) for x in self.__dict__[link_name])})
                elif isinstance(self.__dict__[link_name], str):
                    self.__dict__.update({link_name: int(parse_url_elem(self.__dict__[link_name]))})


class BaseCollection:
    _obj: BaseObject

    def __init__(self, data: list):
        super().__init__()
        self.__storage = {}
        self.__data = data
        self.__feel(data)
        del self.__data

    def __feel(self, data):
        for elm in data:
            obj = self._obj(elm)
            id_ = int(parse_url_elem(obj.url))
            self.__storage.update({id_: obj})

    @property
    def storage(self):
        return self.__storage

    def get(self, id_):
        return self.__storage.get(id_)


class Character(BaseObject):
    _links_list = ["books", "povBooks", "allegiances", "spouse", "mother", "father"]


class CharactersCollection(BaseCollection):
    _obj = Character


class House(BaseObject):
    _links_list = ['currentLord', 'heir', 'overlord', 'founder', 'cadetBranches', 'swornMembers']


class HousesCollection(BaseCollection):
    _obj = House


class Book(BaseObject):
    _links_list = ['characters', 'povCharacters']


class BooksCollection(BaseCollection):
    _obj = Book
