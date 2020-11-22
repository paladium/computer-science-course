#Simple functions
def my_func():
  #Do nothing
  pass

my_func()

#Function with parameters
#a and b should be integers
def my_func_2(a, b):
  #Do nothing
  pass

my_func_2(4, 5)
my_func_2("Hello", "world")

#Do something in a function
def my_func_3(a, b):
  c = a + b
  print(c)

my_func_3(4, 5)
my_func_3(10, 15)
my_func_3("Hello", "world")
my_func_3([1, 2], [5, 6])

#Func with return
def my_func_4(a, b):
  c = a ** b + a * b
  if c > 100:
    #addional calculation
    return 100
    #Cannot do anything after return

  return c

result = my_func_4(3, 4)
print(result)
result2 = my_func_4(10, 15)
print(result2)

#Named arguments
def return_my_profile(name, age):
  return "My name is {} and my age is {}".format(name, age)

profile = return_my_profile("Javid", 16)
print(profile)

profile2 = return_my_profile(age=22, name="Ilkin")
print(profile2)

#Default values
def buy_car(model,insurance=0.1):
  if model == "Audi":
    return 10000 * (1 + insurance)
  elif model == "BMW":
    return 20000 * (1 + insurance)

auto1 = buy_car("Audi")
auto2 = buy_car("BMW")
print(auto1)
print(auto2)
auto3 = buy_car("Audi", 0.2)
print(auto3)
auto4 = buy_car("BMW", insurance=0.3)
print(auto4)