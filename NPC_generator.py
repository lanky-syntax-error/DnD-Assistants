import random
# Race
racelist = ["Human", "Dwarf", "Wood Elf", "High Elf", "Dark Elf", "Orc", "Half-Orc", "Aaracokra", "Goliath", "Halfling"]
race = random.choice(racelist)
# Age
age = random.randint(15, 100)
if race == "Wood Elf" or race == "High Elf":
    age = random.randint(15, 1500)
elif race == "Dark Elf":
    age = random.randint(1, 400)
elif race == "Aaracokra":
    age = random.randint(1, 35)
# Appearance
appearancelist = ["Rugged", "Fair", "Scruffy", "Weedy", "Scraggly", "Polished", "Buff", "Powerful", "Impressive", "Flowery", "Delicate", "Shadowy", "Dishevelled", "Jolly"]
appearance = random.choice(appearancelist)
# Backstory
storylist = ["Soldier", "Farmer", "Artist", "Holy Person", "Vagabond", "Criminal", "Teacher", "Cook", "Outcast", "Slave", "Guard", "Bard"]
story = random.choice(storylist)
# Name
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
name1 = random.choice(letters)
name2 = random.choice(letters)
name3 = random.choice(letters)


print(f"Race: {race}\n")
print(f"Age: {age}\n")
print(f"Background: {story}\n")
print(f"Appearance: {appearance}\n")
print(f"Name Prompt: {name1}{name2}{name3}\n")