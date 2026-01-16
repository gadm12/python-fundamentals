ingredient = input("Enter Ingredient: ").lower().strip()
amount = int(input("enter amount: "))

if ingredient == "mandrake" and amount == 3:
    print("Potion brewing...")

elif ingredient == "nightshade" and amount == 1:
    print("Handle with care...")
elif ingredient == "dragon root" and amount >= 0:
    print("Rare find! Begin preparation...")
else:
    print("Invalid ingredient or incorrect amount")
