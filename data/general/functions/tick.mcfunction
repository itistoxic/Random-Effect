##  Starting or Resetting time
# Adding time
execute if score start time matches 1 run function timer:add/tick


# Resetting if egg if thrown
execute at @p if block ~ ~ ~ nether_portal run scoreboard players set time tick 0

# Ticking
execute if score time tick matches 1 run schedule function timer:tick 1t

# To clear actionbar
execute if score time tick matches 0 run title @a actionbar {"text":"Leaving..."}