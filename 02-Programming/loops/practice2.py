#Guessing game
#Some number, between 0 and 10, a = 5
#Ask a question, enter a number,
#If the entered number equals to a, we print success
#otherwise we keep asking for a correct number
x = 0
y = 10
flag = True
while flag:
  result = (x+y)//2
  answer = input("Is your number " + str(result) + ":" )
  if answer == "yes":
    print("I guessed your number")
    flag = False
  elif answer == "no":
    answer2 = input("If your number is higher than " + str(result) + " enter >. If your number is less than " +str(result) + " print < :")
    if answer2 == '>':
      x = result
    elif answer2 == '<':
      y = result
  