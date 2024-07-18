# Address Book Bot

This is a simple address book bot that allows you to manage your contacts and birthdays.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Moses-93/web_hw_m2.git
```


2. Command for pull image

```bash
docker pull moses93/my_assistant_bot:0.0.1
```

3. Command to start the container
```bash
docker run --name assistant_bot -it --rm -v <your_path>:/web_hw_m2/data moses93/my_assistant_bot:0.0.1
```

## Usage

Once the bot is running, you can interact with it using the following commands:

- `!add <name> <phone> <birthday>`: Add a new contact with a name, phone number, and birthday.
- `!change <name> <old_phone> <new_phone>`: Change the value of a specific field (name, phone, or birthday) for a contact.
- `!show <name>`: Show the contact information for a given name.
- `!add-birthday <name> <birthday>`: Add or update the birthday for a contact.
- `!show-birthday <name>`: Show the birthday for a given name.
- `!del <name>`: Delete a contact from the address book.
- `!phone <name>`: Get the phone number
- `!all <name>`: Get all contacts
- `!birthdays <name>`: Get all birthdays falling within 7 days

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


## UML-diagram

```mermaid
classDiagram
    direction TB

    class AbstractField {
        <<abstract>>
        +value: Any
        +__str__() str
    }

    class AbstractRecord {
        <<abstract>>
        +name: AbstractField
        +phones: list[AbstractField]
        +birthday: AbstractField
        +add_phone(phone: str)
        +remove_phone(phone: str)
        +edit_phone(old_phone: str, new_phone: str)
        +add_birthday(birthday: str)
    }

    class AbstractAddressBook {
        <<abstract>>
        +data: dict[str, AbstractRecord]
        +add_record(record: AbstractRecord)
        +find(name: str) AbstractRecord
        +delete(name: str)
        +get_users_to_greet() list[AbstractRecord]
        
    }


    class Name {
        +value: str
        
    }

    class Phone {
        +value: str
        
    }

    class Birthday {
        +value: str
        
    }

    class Record {
        +name: Name
        +phones: list[Phone]
        +birthday: Birthday
        +add_phone(phone: str)
        +remove_phone(phone: str)
        +edit_phone(old_phone: str, new_phone: str)
        +add_birthday(birthday: str)
        +__str__() str
    }

    class AddressBook {
        +data: dict[str, Record]
        +add_record(record: Record)
        +find(name: str) Record
        +delete(name: str)
        +get_users_to_greet() list[Record]
        +__str__() str
    }

    AbstractField <|-- Name
    AbstractField <|-- Phone
    AbstractField <|-- Birthday

    AbstractRecord <|-- Record

    AbstractAddressBook <|-- AddressBook

    class functions {
        +parse_input(user_input: str) -> tuple
        +add_contact(args: list[str], book: AddressBook) -> str
        +change_contact(args: list[str], book: AddressBook) -> str
        +show_phone(args: list[str], book: AddressBook) -> str
        +add_birthday(args: list[str], book: AddressBook) -> str
        +show_birthday(args: list[str], book: AddressBook) -> str
        +remove(args: list[str], book: AddressBook) -> str
        +load_data(filename: str) -> AddressBook
        +save_data(book: AddressBook, filename: str)
    }

    functions --> AddressBook
