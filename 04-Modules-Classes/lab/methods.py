#Working with class methods
class Aircraft:
  def __init__(self, name, speed):
    self.name = name
    self.speed = speed
  def calculate_time(self, distance):
    return distance/self.speed

plane = Aircraft("F-15", 700)
print("It will take {} hours to fly {} km .".format(plane.calculate_time(2100), 2100))

#1st - make a new plane by asking user for its name and speed
#2nd - ask which distance this plane should travel and output the result
name = input("Enter the name of plane : ")
speed = int(input("Enter the speed : "))
distance = int(input("Enter the distance you will travel : "))
plane2 = Aircraft(name, speed)
print("It will take {} hours for {} to fly {} km .".format(plane2.calculate_time(distance), plane2.name, distance))

#Changing object variables
plane2.speed += 100
plane2.name = "F-16"
print(plane2.speed, plane2.name)

#Song(["I walked during summer", "This does not feel right"])#print_lyrics -> I walked during summer
#                This does not feel right