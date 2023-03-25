import random
import time
print("DICE ROLLER")
print("")
while True:
    DiceRoll = random.randint(1,6)
    DiceRoll = str(DiceRoll)
    if DiceRoll == "1":
        DiceRoll = "one"
    elif DiceRoll == "2":
        DiceRoll = "two"
    elif DiceRoll == "3":
        DiceRoll = "three"
    elif DiceRoll == "4":
        DiceRoll = "four"
    elif DiceRoll == "5":
        DiceRoll = "five"
    elif DiceRoll == "6":
        DiceRoll = "six"
    print("The dice rolled " + DiceRoll + "!")
    time.sleep(1)