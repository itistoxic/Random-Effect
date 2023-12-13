
EFFECT_LENGTH = 60
MAXIMUM_STRENGTH = 10
SECONDS_BETWEEN_EFFECTS = 20


list_of_effects = [
    'Speed',
    'Slowness',
    'Haste',
    'Mining Fatigue',
    'Strength',
    # 'Instant Health',
    # 'Instant Damage',
    'Jump Boost',
    'Nausea',
    'Regeneration',
    'Resistance',
    'Fire Resistance',
    'Water Breathing',
    'Invisibility',
    'Blindness',
    'Night Vision',
    'Hunger',
    'Weakness',
    'Poison',
    'Wither',
    'Health Boost',
    'Absorption',
    'Saturation',
    'Glowing',
    'Levitation',
    'Luck',
    'Bad Luck',
    'Hero of the Village',
    'Slow Falling',
    'Conduit Power',
    'Dolphins Grace',
    'Bad Omen'
]



### -----------------------------------------------

import os
import random
import shutil

DIR = "data/"

shutil.rmtree(DIR + "effect/functions")
os.mkdir(DIR + "effect/functions")

effect_dir = DIR + "effect/functions/"

def format(string : str):
    return string.lower().replace(' ', '_')

for i in range(MAXIMUM_STRENGTH):

    for j in range(len(list_of_effects)):
        command = "effect give @a minecraft:" + format(list_of_effects[j]) + " " + str(EFFECT_LENGTH) + " " + str(i) + " true"

        id =  (i * len(list_of_effects)) + j
        f = open(effect_dir + str(id) + ".mcfunction", "w")

        f.write(command + '\n')
        f.write("say " + format(list_of_effects[j]) + str(i + 1))

        f.close()



#-----

shutil.rmtree(DIR + "tree/functions")
os.mkdir(DIR + "tree/functions")

tree_dir = DIR + "tree/functions/"

def create_tree(low, high):
    if low == high:
        f = open(tree_dir + str(low) + "_" + str(high) + ".mcfunction", "w")
        f.write("""
                function effect:%d
                """ % low
                )
        f.close()
        return
    
    midpoint= int((high - low) / 2 + low)
    
    f = open(tree_dir + str(low) + "_" + str(high) + ".mcfunction", "w")

    f.write( ("execute if score effect rand matches ..%d " % midpoint) + "run function tree:" + str(low) + "_" + str(midpoint) + "\n")
    f.write( ("execute if score effect rand matches %d.. " % (midpoint + 1)) + "run function tree:" + str(midpoint+1) + "_" + str(high) + "\n")

    f.close()

    create_tree(low, midpoint)
    create_tree(midpoint+1, high)
    
COUNT = len(list_of_effects) * MAXIMUM_STRENGTH


# Start function that gets random number
f = open(tree_dir + "start.mcfunction","w")

f.write("""
## Reset time
function timer:reset

# Getting random number
scoreboard players set mod rand %d
function general:rand/num
scoreboard players operation effect rand = num rand
""" % COUNT)

f.write("function tree:0_" + str(COUNT))

create_tree(0, COUNT)