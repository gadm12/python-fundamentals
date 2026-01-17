word = "python"
guess = ""
chances = 3
tries = 0

while guess != word and tries < chances:
    guess = input("guess a word: ")
    tries += 1

if guess == word:
    print("correct")
else:
    print("incorrect, try again!")
