strength = 15
intelligence = 10
agility = 8

job_class = ""

if strength > 10:
    if agility > 10:
        job_class = "Barbarian"
    else:
        job_class = "Warrior"

elif intelligence > 10:
    if agility > 10:
        job_class = "Rogue"
    else:
        job_class = "Mage"

else:
    job_class = "Monk"


print(f"Your class is {job_class}")
