print("--- Simple To-Do List Manager ---")
tasks = []


while True:
    print("")
    print("1- Display tasks list")
    print("2- Add task")
    print("3- Edit task")
    print("4- Delete task")
    print("5- exit")
    command = input("what would you like to do?(enter a number) ")

    if command == "1":
        if not tasks:
            print("No tasks yet")
        else:
            print("Your tasks: ")
            for i, task in enumerate(tasks):
                print(f"{i+1}- {task}")

    elif command == "2":
        new_task = input("enter your task: ")
        tasks.append(new_task)

    elif command == "4":
        if not tasks:
            print("no task to remove")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}- {tasks[i]}")
            remove_request = int(input("Enter the task number: "))
            if 1 <= remove_request <= len(tasks):
                removed_task = tasks.pop(remove_request - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid entry!")

    elif command == "5":
        print("Goodbye")
        break
    else:
        print("Invalid entry!")
