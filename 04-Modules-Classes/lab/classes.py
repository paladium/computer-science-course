#Intro to classes
#inheritance

class Aircraft:
  def __init__(self, name, speed):
    #Self.name - assign value given from the function to the current instance of that clas
    self.name = name
    self.speed = speed

#Instantiate our class - make object of that class
plane = Aircraft("Boeing 747", 700)
print(plane.name)
print(plane.speed)

plane2 = Aircraft("Airbus 500", 800)
print(plane2.name)
print(plane2.speed)