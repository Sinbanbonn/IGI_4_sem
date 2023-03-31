from typing import Set
import re



class CustomCollection(Set):

    __is_loaded = False
    __is_saved = False

    @property
    def is_loaded(self):
        return self.__is_loaded

    @is_loaded.setter
    def is_loaded(self, value):
        self.__is_loaded = value

    @property
    def is_saved(self):
        return self.__is_saved

    @is_saved.setter
    def is_saved(self, value):
        self.__is_saved = value

    def __init__(self, data=()):
        super().__init__(data)

    def find(self, element):
        return element if element in super().copy() else False

    def list(self):
        return [element if not element.isdigit() else int(element) for element in super().copy()]

    def grep(self, pattern):
        return [element for element in super().copy() if re.search(pattern, element)]


