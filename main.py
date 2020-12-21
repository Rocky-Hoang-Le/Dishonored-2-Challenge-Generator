# Dishonored 2 Challenge Creator
# Goal of this project is to have a random generator of mission goals and powers for the iron playthrough
# If you fail the play style goals you must die and start a new randomized iron playthrough
# I made an exception for bonecraft power so you can play through with crafted bonecharms and dark vision isn't allowed (I don't play with it)

import random
from random import shuffle
from random import randint

# Active powers List
mobilitylist = ["[Far Reach]", "[Blink]", "[No Mobility powers]"]
powerslist = ["[Bend Time]", "[Devouring Swarm]", "[Possession]", "[Mesmerize]", "[Domino]", "[Shadow Walk]", "[Doppelganger]"]
shuffle(powerslist)

# Passive Powers list
passpowerslist = ["[Agility]", "[Blood Thirst]", "[Reflexes]", "[Shadow Kill]", "[Strength]", "[Vitality]"]
shuffle(passpowerslist)

# Play Style list
playlist = ["[Kill]", "[Not Kill]"]


# Intro print line
print("Welcome to Dishonored 2 Random playthrough generator!\nHere are your randomly generated powers and play style!\n")

# Print allowed mobile powers
print("Mobility Ability\n" + mobilitylist[randint(0, 2)] + "\n")

# Set the random num gen range from 1- however many powers you want allowed max to generate ( i set max to 3 so runs wont be too easy)
# Print Allowed Active Powers
print("Active Powers")
for x in range(randint(1, 3)):
    print(powerslist[x - 1] + " ")

# Print Allowed Passives Powers
print("\nPassive Powers")
for x in range(randint(1, 3)):
    print(passpowerslist[x - 1] + " ")

# Print Play style
print("\nIn this playthrough you may " + playlist[randint(0, 1)])