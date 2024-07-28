from random import randint
from time import sleep
rollagain = "peeny-weeny"

while rollagain != "DONE":
    num = input("HOW MANY DICE? ")
    num = int(num)
    val = input("WHAT DICE VALUE? ")
    val = int(val)
    mod = input("MODIFIER: ")
    mod = int(mod)

    # The roll
    rolls = []
    counter = int(num)
    while counter != 0:
        roll = (randint(1, val))
        rolls.append(roll)
        counter -= 1
        print(roll)
        sleep(0.5)

    total = sum(rolls)
    total1 = (total + mod)
    print(f"TOTAL: {total} + MODIFIER OF {mod} =")
    sleep(0.5)
    print(f"{total1}!")

    rollagain = input("PRESS ENTER TO ROLL AGAIN OR TYPE'DONE' TO FINISH: ")