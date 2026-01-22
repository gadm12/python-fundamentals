print("Welcome to the TODO List app!")
tasks = []


while True:
    print("1- Add task")
    print("2- Display")
    print("3- Edit")
    print("4- Delete")
    print("5- e")
    command = input("what would you like to do?(enter a number) ")

    if command == "1":
        task = input("what task would you like to add: ")
        tasks.append(task)
    if command == "2":
        for i, j in enumerate(tasks):
            print(f"{i+1}- {j}")
