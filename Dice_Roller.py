# Making a dice rolling simulator
# Monday 8th February 2021 - 19:16
# George Koundouri

# Importing the relevant imports
import random

while True:
    player = input("Would you like to roll a die? ").lower()
    if player == "no":
        print("As you wish. Goodbye! ")
        break
    elif player == "yes":
        print("Very well, good luck! ")
        print(random.randint(0, 5))
    else:
        print("Please check your spelling!")
