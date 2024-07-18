from address_book.implementation_of_classes import AddressBook, Record, Birthday
import pickle

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError as error:
            return f"Contact with the name was not found: {error}"
        except ValueError as error:
            return f"You did not specify a name, phone number, or date of birth correctly: {error}"
        except IndexError as error:
            return f"Please enter the name and phone number: {error}"
        except Exception as error:
            return f"An unexpected error occurred: {error}"
    return inner

@input_error
def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

@input_error
def add_contact(args, book):
    try:
        name, phone = args
        if name in book:
            book[name].add_phone(phone)
            return "Phone added to existing contact"

        else:
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            return "New contact added"
    except Exception as e:
        return e
    
@input_error
def change_contact(args, book): 
        name, old_phone, new_phone = args
        try:
            if name not in book or len(new_phone) !=10:
                raise ValueError(f"Incorrect phone number: {new_phone}")
            else:
                record = book[name]
                record.edit_phone(old_phone, new_phone)
                return "Contact updated." 
        except Exception as e:
            return e
    
@input_error   
def show_phone(args, book):
    *_, name = args
    return book[name]

@input_error
def add_birthday(args, book):
    name, birthday = args
    if name in book:
        record = book[name]
        record.add_birthday(birthday)
        return "Birthday added"
    else:
        return "Contact not found"

@input_error
def show_birthday(args, book):
    *_, name = args
    if name in book:
        record = book[name]
        if record.birthday:
            return record.birthday.value
        else:
            return "Birthday not found for this contact"
    else:
        return "Contact not found"
    
@input_error  
def remove(args, book):
    *_, name = args
    if name in book:
        book.delete(name)
        return "The contact has been deleted"

    else:
        return f"Contact '{name}' not found"
    
@input_error
def load_data(filename="data/addressbook.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
    except EOFError: # Додаємо обробку EOFError, якщо файл існує, але порожній
        return AddressBook()

@input_error
def save_data(book, filename="data/addressbook.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)

