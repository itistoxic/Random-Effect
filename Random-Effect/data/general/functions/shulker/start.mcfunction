# Clearing inventory
clear @p

# Giving items
setblock 0 250 0 yellow_shulker_box

data modify block 0 250 0 Items set from storage chest 1

execute at @p run loot give @p mine 0 250 0 minecraft:air{drop_contents: 1b}

setblock 0 250 0 air

# Removing glass and random items
clear @p light_gray_stained_glass_pane