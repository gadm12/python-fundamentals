character = {"name": "Thorn", "class": "Rogue"}
# New class: "Ranger"

change_request = input("would like to change your class? ")

if change_request == "yes":
    new_class = input("which class would you like to choose (Warrior, Ranger)? ")
    character["class"] = new_class
    print(f"{character['name']} is now {character['class']}")
else:
    print("Class change refused")
