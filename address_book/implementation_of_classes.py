from address_book.abstract_classes import (AbstractField, AbstractAddressBook, AbstractRecord)
from datetime import datetime, timedelta


class Name(AbstractField):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)



class Phone(AbstractField):

    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number should be 10 digits")
        super().__init__(value)


class Birthday(AbstractField):
    def __init__(self, value):
        try:
            today = datetime.now().date() #теперішня дата 
            value = datetime.strptime(value, '%d.%m.%Y').date() #перевоодимо дату в об'єкт datetime
            value = datetime(today.year, value.month, value.day).date() #готуємо дату для подальшого порівння, додавши теперішній рік
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        

class Record(AbstractRecord):
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = None
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def find_phone(self, phone):
        index = self.phones.index(phone)
        try:
            return self.phones[index]
        except ValueError:
            print("No such phone number found")

    def edit_phone(self, old_phone, new_phone):
        phone_str_list = [str(phone) for phone in self.phones]
        if old_phone in phone_str_list:
            index = phone_str_list.index(old_phone)
            self.phones[index] = Phone(new_phone)
        else:
            print("No such phone number found")

    def remove_phone(self, phone):
        if phone not in self.phones:
            print("No such phone number found")
        else:
            self.phones.remove(phone)

    def __str__(self):
        # Повертаємо рядок, який містить ім's користувача та його номери телефону
        return f"Контакт: {self.name}, Телефони: {', '.join(str(p) for p in self.phones)}, День народження: {self.birthday}"



class AddressBook(AbstractAddressBook):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
            del self.data[name]
            

    def get_users_to_greet(self):
        today = datetime.today().date() 
        users_to_greet = []
        for _, record in self.data.items():
            try:
                if record.birthday.value - today >= timedelta(days=0) and record.birthday.value - today <= timedelta(days=7):
                    users_to_greet.append(record)
            except AttributeError: # обробка вийнятків, для тих контактів, в яких не вказане день народження 
                pass
        if not users_to_greet:  # Якщо список порожній, виводимо відповідне повідомлення
            print("No upcoming birthdays found.")
        return users_to_greet
    
    def __str__(self):
        re = [record for _, record in self.data.items()]
        return "\n".join(str(r) for r in re)
    
