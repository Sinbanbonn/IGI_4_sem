import os
import re
from storage import CustomCollection
class DataStorage:

    def __init__(self):
        self.data = {}

    def user_exists(self, username):
        try:
            user_data = self.data[username]
            return True
        except KeyError:
            return False

    def add_user(self, username):
        self.data[username] = CustomCollection()

    def add_element(self, username, element):
        self.data[username].add(element)
        self.data[username].is_saved = False

    def remove_element(self, username, element):
        self.data[username].remove(element)
        self.data[username].is_saved = False

    def find_element(self, username, element):
        return self.data[username].find(element)

    def grep_element(self, username, reg_exp):
        try:
            return self.data[username].grep(reg_exp)
        except re.error:
            return None

    def get_elements_list(self, username):
        return self.data[username].list()

    def save_data(self, username):

        with open('storage.txt', 'r+') as file:
            with open('output.txt', 'w+') as f:
                for line in file:
                    if line and line.split(':')[0] != username:
                        f.write(line.replace("\n", "") + "\n")
                    elif line.split(':')[0] == username:
                        if not self.data[username].is_loaded:
                            self.add__few_elements(username, line.split(':')[1][1:].split(' • '))
                elements = f"{username}: " + " • ".join(self.data[username])
                f.write(elements)
                self.data[username].is_saved = True
        os.remove('storage.txt')
        os.rename('output.txt', 'storage.txt')

    def load_data(self, username):

        with open('storage.txt', 'r') as file:
            for line in file:
                if line.split(':')[0] == username:
                    data = "".join(line.split(': ')[1:]).split(" • ")
                    self.add__few_elements(username, data)
                    self.data[username].is_loaded = True
                    return True

        return False

    def add__few_elements(self, username, elements):

        if self.user_exists(username):
            for element in elements:
                if element:
                    element = element.replace("\n", "")
                    self.data[username].add(element)
        else:
            self.data[username] = CustomCollection(elements)

    def is_saved(self, username):
        return self.data[username].is_savedclass

    def __init__(self):
        self.data = {}

    def user_exists(self, username):
        try:
            user_data = self.data[username]
            return True
        except KeyError:
            return False

    def add_user(self, username):
        self.data[username] = CustomCollection()

    def add_element(self, username, element):
        self.data[username].add(element)
        self.data[username].is_saved = False

    def remove_element(self, username, element):
        self.data[username].remove(element)
        self.data[username].is_saved = False

    def find_element(self, username, element):
        return self.data[username].find(element)

    def grep_element(self, username, reg_exp):
        try:
            return self.data[username].grep(reg_exp)
        except re.error:
            return None

    def get_elements_list(self, username):
        return self.data[username].list()

    def save_data(self, username):

        with open('storage.txt', 'r+') as file:
            with open('output.txt', 'w+') as f:
                for line in file:
                    if line and line.split(':')[0] != username:
                        f.write(line.replace("\n", "") + "\n")
                    elif line.split(':')[0] == username:
                        if not self.data[username].is_loaded:
                            self.add__few_elements(username, line.split(':')[1][1:].split(' • '))
                elements = f"{username}: " + " • ".join(self.data[username])
                f.write(elements)
                self.data[username].is_saved = True
        os.remove('storage.txt')
        os.rename('output.txt', 'storage.txt')

    def load_data(self, username):

        with open('storage.txt', 'r') as file:
            for line in file:
                if line.split(':')[0] == username:
                    data = "".join(line.split(': ')[1:]).split(" • ")
                    self.add__few_elements(username, data)
                    self.data[username].is_loaded = True
                    return True

        return False

    def add__few_elements(self, username, elements):

        if self.user_exists(username):
            for element in elements:
                if element:
                    element = element.replace("\n", "")
                    self.data[username].add(element)
        else:
            self.data[username] = CustomCollection(elements)

    def is_saved(self, username):
        return self.data[username].is_saved