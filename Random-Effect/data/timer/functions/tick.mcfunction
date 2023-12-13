
## Potion effect every x seconds
execute if score second time matches 20 run function tree:start

# Adding time
function timer:add/tick

# Ticking
execute if score time tick matches 1 run schedule function timer:tick 1t
