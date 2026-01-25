print("--- Simple Contact Book ---")
contacts = {}

while True:
    print("")
    print("1- Display contacts list")
    print("2- Add contact")
    print("3- Search contact")
    print("4- Edit contact")
    print("5- Delete contact")
    print("6- exit")
    choice = input("choose an option between (1-4): ")

    if choice == "1":
        if not contacts:
            print("The contact book is empty")
        else:
            for name in contacts:
                print(f"Name: {name}, Phone: {contacts[name]}")

    elif choice == "2":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts[name] = phone
        print(f"Contact for {name} added.")

    elif choice == "3":
        search_name = input("Enter the name to search for: ")
        if search_name in contacts:
            print(f"Found: {search_name} - {contacts[name]}")
        else:
            print("contact does not exist")

    elif choice == "4":
        break

    elif choice == "5":
        break

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid entry!")
