#Solar system analyser
#You enter a number of planets you have in your system
#e.g -5,6
#You ask for that number of planets to enter, Xander, Death Star
#Add all those planets to a list of planets
#Print all the planets
plan_num = int(input("Enter the number of planets your system has : "))
planets = []
for planet in range(1, plan_num + 1):
  name = input("What is the name of planet {} : ".format(planet))
  planets.append(name)
print(planets)
question = input("Do you want to destroy any of these planets ? : ")
if question == "yes":
  how_many = int(input("How many planets will be destroyed ? - "))
  for target in range(how_many):
    destroy = input("Enter the name of planet you want to destroy : ")
    planets.remove(destroy)
    print("{} planet is destroyed !".format(destroy))
print(planets)    
  
#Question asked, do you want to destroy any of the planets? yes or no
#yes -> how many planets to destroy - 3
#You enter the name of the planet the destroy
#After each time you destroy a planet you print the current list of planets