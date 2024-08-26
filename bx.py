class ContactManager:
    def _init_(ahmed):
        ahmed.contacts = {}

    def add_contact(ahmed, name, phone_number):
        ahmed.contacts[name] = phone_number
        print(f"Contact '{name}' added with phone number{phone_number}")
    def remove_contact(ahmed, name):
        if name in ahmed.contacts:
            del ahmed.contacts[name]
            print(f"Contact '{name}' removed successfuly")
        else:
            print(f"Contact '{name}' not found")
    def search_contacts(ahmed, name):
        if name in ahmed.contacts:
            print(f"Name: {name}, Phone Number:{ahmed.contacts[name]}")
        else:
            print(f"Contact '{name}' not found")

    def view_all_contacts(ahmed):
        if ahmed.contacts:
            print("All Contacts: ")
            for name, phone_number in ahmed.contacts.items():
                print((f"Name: {name}, Phone Number: {phone_number}"))
            else:
                print("No contacts found")

    def update_contact_phone(ahmed, name, new_phone_number):
        if name in ahmed.contacts:
            ahmed.contacts[name] = new_phone_number
            print(f"Phone number updated for contact '{name}'")
        else:
            print(f"Contact'{name}' not found")

if __name__ == "_main_":
    manager = ContactManager

    manager.add_contact("Aly", "123-456-7890")
    manager.add_contact("Omar", "123-0987-546")

    manager.view_all_contacts()

    manager.update_contact_phone("Aly", "000-000-000")

    manager.search_contacts("Omar")

    manager.remove_contact("Aly")

    manager.view_all_contacts()