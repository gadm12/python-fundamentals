def choose_path():
    option = int(
        input("Which path will you take? 1. Forest, 2. Mountains, 3. Desert? ")
    )

    if option == 1:
        print("You have chosen the forest path.")
    elif option == 2:
        print("You have chosen the mountain path.")
    elif option == 3:
        print("You have chosen the desert path.")
    else:
        print("invalid entry!")
    return option


choose_path()
