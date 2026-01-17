run_count = 0
action = ""
while run_count < 3:
    action = input("Type your action: ")

    if action == "run":
        run_count += 1
    else:
        print("That will not help you")

print("You escape the cave safely!")
