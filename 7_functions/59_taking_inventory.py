def take_inventory(items):

    for item in items:
        print(f"You have: {item}")
    return items


items_list = ["sword", "shield", "potion"]
take_inventory(items_list)
