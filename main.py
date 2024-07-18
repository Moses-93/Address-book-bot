from address_book import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    add_birthday,
    show_birthday,
    remove,
    load_data,
    save_data,
)

def main():
    book = load_data()
    print("Welcome to assistant bot")

    while True:

        user_input = input("Enter a command: ")
        cmd, *args = parse_input(user_input)

        if cmd == "hello":
            print("How can I help you")

        elif cmd in ["close", "exit"]:
            print("Good bye")
            save_data(book)
            break

        elif cmd == "add":
            print(add_contact(args, book))

        elif cmd == "phone":
            print(show_phone(args, book))

        elif cmd == "change":
            print(change_contact(args, book))

        elif cmd == "all":
            if book:
                print(book)
            else:
                print("Address book is empty")

        elif cmd == "add-birthday":
            print(add_birthday(args, book))

        elif cmd == "show-birthday":
            print(show_birthday(args, book))

        elif cmd == "birthdays":
            for el in book.get_users_to_greet():
                print(f"{el.name} {el.birthday}")

        elif cmd == "del":
            print(remove(args, book))

        else:
            print("invalid command")

if __name__ == "__main__":
    main()