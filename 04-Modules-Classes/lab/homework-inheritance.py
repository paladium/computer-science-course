class Transport:
  def __init__(self, name, top_speed):
    self.name = name
    self.top_speed = top_speed

class Airplane(Transport):
  def __init__(self, name, top_speed, max_altitude):
    super().__init__(name, top_speed)
    self.max_altitude = max_altitude

class Car(Transport):
  def __init__(self, name, top_speed, engine_type):
    super().__init__(name, top_speed)
    self.engine_type = engine_type

plane = Airplane("JH-21", 200, 2004)
print(plane.name, plane.top_speed, plane.max_altitude)
car = Car("BMW", 200, "Six Cylinders")
print(car.name, car.top_speed, car.engine_type)

#Parent class - Transport
#Car and Airplane
##Well done - 10/10