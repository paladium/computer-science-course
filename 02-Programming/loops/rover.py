# Rover example using while loop
#Enter the current position: -100, 100, check between those values, if invalid output invalid
#Input if we found water at current position, yes: no
#If yes, then we continue looking for 1 point, we keep asking the question if we found water at that position
#At the end, for each position, we add one point that we found water
#Output the total number of points of water
#---xxOx- 4 points
# Enter the current position of rover: -> 5
# Is there water at current position 5? -> yes
# Is there water at position 6? -> yes
# Is there water at position 7? -> no
# Is there water at position 4? -> yes
# Is there water at position 3? -> no
# The total points is: 3

##Additional, we extend it to two dimensional. x, x and y
# Instead of moving, left and right, x+1, x -1, y - 1, y + 1
# Initial position - 4, 4
# Is there water at position (5, 4) -> yes
# Is there water at position (6, 4) -> no
# (3, 4) -> no
# (4, 5) -> no
# (4, 3) -> no