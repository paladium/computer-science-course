function = input("Fucntion : ")
if function == "1":
  def find_average(a):
    sum = 0
    for number in a:
      sum += number
    average = sum/len(a)
    print(average)
  numbers = [12, 32, 45, 67]
  find_average(numbers)
elif function == "2":
  def find_factorial(number):
    multiply = 1
    if number == 0:
      print(multiply)
    elif number > 0:
      for num in range(1, number+1):
        multiply *= num
      print(multiply)
  find_factorial(0)
  find_factorial(1)
  find_factorial(7)
  #find_factorial(100)
elif function == "3":
  def identify_case(string):
    upper = 0
    lower = 0
    for letter in string:
      if letter.isupper():
        upper += 1
      else:
        lower += 1
    print("Letters with upper_case : {}\nLetters with lower_case : {}".format(upper, lower))
  identify_case("HadInHSiuhSIUhuIO")
elif function == "4":
  def find_evens(lis):
    even_numbers = []
    for number in lis:
      if number%2 == 0:
        even_numbers.append(number)
    print(even_numbers)
  abc = [3, 6, 90, 34, 5, 7]
  find_evens(abc)
elif function == "5":
  def evens_in_range():
    a = int(input("First number : "))
    b = int(input("Second number : "))
    evens = []
    for number in range(a, b+1):
      if number%2 == 0:
        evens.append(number)
    return evens
  print(evens_in_range())

#Grade - 100/100