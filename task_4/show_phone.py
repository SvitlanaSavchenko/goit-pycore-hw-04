def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."