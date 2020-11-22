#Read from a file
#Push all the items from the file into a list
#Add a new element
#Write to the file - same file
lis = []
with open("testfile.txt") as file:
  for element in file:
    lis.append(element.strip())
  user = input("Enter the element : ")
  lis.append(user)

with open("testfile.txt", "w") as file: 
  for item in lis:
    file.write(item + "\n") 

import os
filename = input("Enter the name of the file you want to remove : ")
if os.path.exists(filename):
  os.remove(filename)
else:
  print("This file does not exist !!!")