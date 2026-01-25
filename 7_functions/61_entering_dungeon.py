def enter_dungeon():
    print("You enter a dark and musty dungeon.")
    print("The air is cold, and you hear distant growls.")
    path = input("Would you like to continue or leave the dungeon? ")
    if path == "continue":
        print("You continue deeper in the Dungeon...")
    elif path == "leave":
        print("you leaving the Dungeon")
    return path


enter_dungeon()
