from time import sleep

charlist = {}
initlist = {}
charname = ""
currentchar = ""


# INPUTS
while charname != "DONE":
    charname = input(f"Add character name here, or type 'DONE' to finish:\n")
    if charname == "DONE":
        break
    charhp = input(f"What is {charname}'s current HP?\n")
    charlist[charname] = charhp
    charinit = input(f"What is {charname}'s initiative roll?\n")
    initlist[charname] = charinit

# MAX HP
hpcap = charlist.copy()


# LISTINGS
initsort = sorted(initlist.items(), key=lambda item: int(item[1]), reverse=True)

print(f"\nPLAYERS:")
for charname, charhp in charlist.items():
    print(f"{charname}: {charhp} HP")
    sleep(0.5)

print(f"\nINITIATIVE:")
for charname, charinit in initsort:
    print(f"{charname}: {charinit}")
    sleep(0.5)


# START COMBAT 
combatbgn = input(f"Ready to begin combat? (Y/N?)\n")
while combatbgn != "Y":
    
    if combatbgn == "N":
        print("Putting off the inevitable...")
        sleep(1)
        combatbgn = input(f"Ready now? (Y/N?)\n")

    elif combatbgn != "Y" and combatbgn != "N":
        combatbgn = input(f"INVALID ANSWER. Please enter 'Y' or 'N':\n")
    
    elif combatbgn == "Y":
        break

# COMBAT
turn = 0
print("COMBAT BEGINS!")
player = "Nobody"
while player != "FINISH":
    player = input(f"\nSelect character to take damage/heal or type 'FINISH' to end combat:\n")
    if player in charlist:
        dmgheal = input(f"Damage or heal {player}, (D/H?)\n")
        if dmgheal == "D":
            dmg = int(input(f"What amount of damage does {player} take?\n"))
            charlist[player] = int(charlist[player]) - dmg
            if int(charlist[player]) < 0:
                charlist[player] = 0
                print(f"{player} IS DOWN!")
            print(f"{player} has {charlist[player]} HP remaining!\n")
        elif dmgheal == "H":
            heal = int(input(f"How many points does {player} heal for?\n"))
            charlist[player] = int(charlist[player]) + heal
            if int(charlist[player]) > int(hpcap[player]):
                charlist[player] -= int(charlist[player]) - int(hpcap[player])
            print(f"{player} is up to {charlist[player]} HP!")
    elif player not in charlist and player != "FINISH":
        print(f"INVALID CHARACTER NAME\n")


# FINISH
print("COMBAT OVER! FINAL RESULTS:")
for charname, charhp in charlist.items():
    print(f"{charname}: {charhp} HP")
    sleep(0.5)