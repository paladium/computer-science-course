#Our main application
#First of all input values from the terminal
#Ask user how many numbers to input - 4, 5
#Next ask for n numbers and store them in the list
import calculator
from more_calc import average, PI#from import
import math
how_many = int(input("How many numbers are you goin to input : "))
numbers = []
for i in range(1, how_many+1):
  num = int(input("Enter the number : "))
  numbers.append(num)
print(numbers)
print(calculator.sum(numbers))
print(average(numbers))
print(PI)
print(math.sin(0.5))
print(math.cos(-0.5))