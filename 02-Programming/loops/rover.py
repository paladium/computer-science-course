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

cur_pos = int(input("Enter your current position : "))
initial = cur_pos
flag = True
water_num = 0
while flag:
  if -100 <= cur_pos <= 100:
    water_check = input("Is there water at position {} ? ".format(initial))
    if water_check == "yes":
      if initial >= cur_pos:
        initial += 1
      elif initial < cur_pos:
        initial -=1
      water_num += 1
    elif water_check == "no":
      if initial >= cur_pos:
        initial = cur_pos - 1
      elif initial < cur_pos:
        flag = False
  else:
    print("Invalid position !")
    break
print("{} places with water were found .".format(water_num))
  