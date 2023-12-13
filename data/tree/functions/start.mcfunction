
## Reset time
function timer:reset

# Getting random number
scoreboard players set mod rand 300
function general:rand/num
scoreboard players operation effect rand = num rand
function tree:0_300