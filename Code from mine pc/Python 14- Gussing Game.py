import random
from random import randint


i="yes"



print("if you want to play the game type : yes and type : no for exit")
Play = (input("Enter yes/no:"))
while Play == ("yes" or "yes"):

        exit
        num = int(input("Enter any Number 1-5:"))
        guess = random.randint(1,5)

        if num == guess:
                print("You win")
                print(f"your input :{num} is match with {guess}")

        elif num != guess:
                print("You Loss")
                print(f"your input :{num} is  not match with {guess}")




