character = {"name": "Aria", "level": 5, "health": 40}
count = 3

while count > 0:
    character["health"] = character["health"] - 10
    count -= 1
print(f"Updated health: {character["health"]}")
