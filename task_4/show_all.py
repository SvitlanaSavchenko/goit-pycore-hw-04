def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts available."