def restore_health(current_health, potion):

    health = current_health + potion

    return health


new_health = restore_health(50, 20)
print(f"New health: {new_health}")
