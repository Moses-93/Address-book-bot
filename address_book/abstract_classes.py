from collections import UserDict
from abc import ABC, abstractmethod

class AbstractField(ABC):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class AbstractRecord(ABC):
    
    @abstractmethod
    def add_phone(self, phone):
        pass

    @abstractmethod
    def add_birthday(self, bierhday):
        pass
    
    @abstractmethod
    def find_phone(self, phone):
        pass

    @abstractmethod
    def remove_phone(self, phone):
        pass

    @abstractmethod
    def edit_phone(self, old_phone, new_phone):
        pass


class AbstractAddressBook(ABC, UserDict):
    
    @abstractmethod
    def add_record(self, record):
        pass

    @abstractmethod
    def find(self, name):
        pass

    @abstractmethod
    def delete(self, name):
        pass

    @abstractmethod
    def get_users_to_greet(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
