def deal_damage(health, damage):

    new_health = health - damage
    print(f"Enemy has {new_health} health left")

    return health, damage


deal_damage(100, 25)
