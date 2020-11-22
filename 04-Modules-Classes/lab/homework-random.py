import random
part = int(input("Part : "))
if part == 1:
  while True:
    a = random.randrange(1, 101)
    #print(a)
    user = int(input("Enter the number that you think our program generated : "))
    if user == a:
      print("Congratulations you predicted correctly . The number is {} ".format(a))
      break
    else:
      print("No the number is {}".format(a))
      continue
  #10/10
elif part == 2:
  #10**8,10**9
  print(random.randrange(10000000, 1000000000))
  #10/10
elif part == 3:
  string = input("Enter a string : ")
  random_c = random.choice(string)
  print(random_c)
  #10/10
elif part == 4:
  answer = "roll"
  total = 0
  while answer == "roll":
    new_number = random.randrange(1, 7)
    print(new_number)
    total += new_number
    answer = input("Enter 'roll' to continue : ")
  print(total)
  #10/10
elif part == 5:
  how_many = int(input("Enter the number of dices you will roll at the same time"))
  answer = "roll"
  total = 0
  while answer == "roll":
    for i in range(1, how_many + 1):
      new_number = random.randrange(1, 7)
      print(new_number)
      total += new_number
    answer = input("Enter 'roll' to continue : ")
  print(total)
  #10/10
elif part == 6:
  letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
  new_password = ""
  password_elements = []
  length = int(input("Enter the length of new password : "))
  l_number = length // 2
  print(l_number)
  n_number = length - l_number
  print(n_number)
  for i in range(1, l_number+1):
    r_letter = random.choice(letters)
    print(r_letter)
    password_elements.append(r_letter)
  for i in range(1, n_number+1):
    r_number = str(random.randrange(0, 10))
    print(r_number)
    password_elements.append(r_number)
  random.shuffle(password_elements)
  for element in password_elements:
    new_password += element
  print(new_password)
  ##10/10