attack_roll = 17
armor_class = 15

results = attack_roll - armor_class
print(f"Attack Roll: {attack_roll}")
print(f"Enemy Armor Class (AC): {armor_class}")

if results > 0:
    print("Hit!")
