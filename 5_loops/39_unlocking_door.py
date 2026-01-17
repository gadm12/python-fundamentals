guess = ""

secret_word = "open"

while guess != secret_word:
    guess = input("Enter password: ")
    if guess == secret_word:
        print("The door unlocks with a flash of light")
    else:
        print("the door doesn't budge..")
