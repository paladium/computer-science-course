##Additional, we extend it to two dimensional. x, x and y
# Instead of moving, left and right, x+1, x -1, y - 1, y + 1
# Initial position - 4, 4
# Is there water at position (5, 4) -> yes
# Is there water at position (6, 4) -> no
# (3, 4) -> no
# (4, 5) -> no
# (4, 3) -> no
#Finish for tomorrow's lesson - advanced 2D plane
x = int(input("Enter your x coordinate : "))
initialx = x
y = int(input("Enter your y coordinate : "))
initialy = y
flag = True
water_num = 0
while flag:
  if -100 <= x <= 100 and -100 <= y <= 100:
    water_check = input("Is there water at position ({}, {}) ? ".format(initialx, y))
    if water_check == "yes":
      if initialx >= x:
        initialx += 1
      elif initialx < x:
        initialx -=1
      water_num += 1
    elif water_check == "no":
      if initialx >= x:
        initialx = x - 1
      elif initialx < x:
        #We can to x, y + 1
        flag = False
  else:
    print("Invalid position !")
    break
flag = True
initialx = x
initialy = y +1
while flag:
  water_check = input("Is there water at position ({}, {}) ? ".format(x, initialy))
  if water_check == "yes":
    if initialy >= y:
      initialy += 1
    elif initialy < y:
      initialy -=1
    water_num += 1
  elif water_check == "no":
    if initialy >= y:
      initialy = y - 1
    elif initialy < y:
      flag = False
print("{} places with water were found .".format(water_num))