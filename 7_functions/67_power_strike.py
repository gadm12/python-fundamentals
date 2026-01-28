def buff_stat(strength, buff):

    return strength + buff


def calculate_damage(multiplier):

    return buff_stat(10, 5) * multiplier


total_damage = calculate_damage(2)
print(f"You dealt {total_damage} damage!")
