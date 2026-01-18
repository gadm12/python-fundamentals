inventory = {"weapon": "Sword", "empty": "", "potion": "Healing"}

for key in list(inventory.keys()):

    if key == "empty":
        del inventory[key]
    else:
        print(f"The following will not be removed: {key}")

print(f"Updated Inventory: {inventory}")
