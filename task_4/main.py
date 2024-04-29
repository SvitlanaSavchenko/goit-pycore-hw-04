from parse_input import parse_input
from add_contact import add_contact
from change_contact import change_contact
from show_phone import show_phone
from show_all import show_all

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("You can use some of this comand:\n hello \n add [ім'я] [номер телефону] \n change [ім'я] [новий номер телефону] \n phone [ім'я] \n all \n close or exit. \n Let`s go!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(contacts, *args))
            else:
                print("Invalid command.")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(contacts, *args))
            else:
                print("Invalid command.")
        elif command == "phone":
            if len(args) == 1:
                print(show_phone(contacts, *args))
            else:
                print("Invalid command.")
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()