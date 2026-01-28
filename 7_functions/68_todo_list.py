def show_menu():
    print("")
    print("1- Display tasks list")
    print("2- Add a task")
    print("3- Edit a task")
    print("4- Remove a task")
    print("5- exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet")
    else:
        print("Your tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}- {task}")


def add_tasks(tasks):

    new_task = input("enter your task: ")
    tasks.append(new_task)
    return tasks


def remove_tasks(tasks):
    view_tasks(tasks)
    remove_request = int(input("Enter the task number: "))
    if 1 <= remove_request <= len(tasks):
        removed_task = tasks.pop(remove_request - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid entry!")


tasks = []
print("--- Simple To-Do List Manager ---")
while True:

    show_menu()
    command = input("what would you like to do?(enter a number) ")

    if command == "1":
        view_tasks(tasks)

    elif command == "2":
        add_tasks(tasks)
        print("Task added")

    elif command == "4":
        remove_tasks(tasks)

    elif command == "5":
        print("Goodbye")
        break
    else:
        print("Invalid entry!")
