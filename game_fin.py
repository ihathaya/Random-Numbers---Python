import sys
from random import randint
print("The goal is to pick a number between 1 to 5 on easy, 1 to 10 on medium and 1 to 20 on hard, if it matches with the random run, you win!")
print("")
print("Lets play!")
print("")
mod = input("Choose difficulty - easy, medium or hard > ")
try:
    if mod == "easy":
        try:
            while randint(1,5):
                inp = eval(input("Your guess: "))
                if inp != randint(1,5):
                    print("Not there yet")
                    print("This round was ", randint(1,5))
                    continue
                elif inp == randint(1,5):
                    print("That´s correct!")
                    break
            quit()
        except:
            print("Not a valid input")
            quit()
    elif mod == "medium":
        try:
            while randint(1,10):
                inp = eval(input("Your guess: "))
                if inp != randint(1,10):
                    print("Not there yet")
                    print("This round was ", randint(1,10))
                    continue
                elif inp == randint(1,10):
                    print("That´s correct!")
                    break
            quit()
        except:
            print("Not a valid input")
    elif mod == "hard":
        try:
            while randint(1,20):
                inp = eval(input("Your guess: "))
                if inp != randint(1,20):
                    print("Not there yet")
                    print("This round was "), randint(1,20)
                    continue
                elif inp == randint(1,20):
                    print("That´s correct!")
                    break
            quit()
        except:
            print("Input not valid")
except:
    print("Input not valid")
    
