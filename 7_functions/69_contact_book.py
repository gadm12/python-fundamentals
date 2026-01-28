def show_contact_menu():
    print("option")
    print("1- Display contacts list")
    print("2- Add contact")
    print("3- Search contact")
    print("4- Edit contact")
    print("5- Delete contact")
    print("6- exit")


def view_contacts(contacts):
    if not contacts:
        print("The contact book is empty")
    else:
        for name in contacts:
            print(f"Name: {name}, Phone: {contacts[name]}")


def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact for {name} added.")


def search_contact(contacts):

    search_name = input("Enter the name to search for: ")
    if search_name in contacts:
        print(f"Found: {search_name} - {contacts[search_name]}")
    else:
        print("contact does not exist")


print("--- Simple Contact Book ---")
contacts = {}

while True:

    show_contact_menu()

    choice = input("choose an option between (1-6): ")

    if choice == "1":
        view_contacts(contacts)

    elif choice == "2":
        add_contact(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        break

    elif choice == "5":
        break

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid entry!")
