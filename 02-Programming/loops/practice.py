#Input the name of the school
# Input the number of classes you have in a school
#Output, each class, assuming we have 3 groups - A, B, C
# Input - #51, 5 classes - 1, 2, 3, 4, 5
# Output - 1A, 1B, 1C, 2A, 2B, 2C etc.
#Check if the num_classes bigger than zero and smaller than 12, continue our program, otherwise we print invalid input
school = input("Enter the name of the school : ")
num_classes = int(input("Enter the number of classes you have : "))
if 0 < num_classes < 12: 
  for num in range(1, num_classes+1):
    print(str(num) + "A")
    print(str(num) + "B")
    print(str(num) + "C")
else:
  print("You entered incorrect number of classe.")
  
