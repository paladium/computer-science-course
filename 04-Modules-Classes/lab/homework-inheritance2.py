class Planet:
  def __init__(self, name, radius):
    self.name = name
    self.radius = radius
  def introduce(self):
    print("Planet name : {}\nPlanet's radius : {} km\n".format(self.name, self.radius))

class LivingPlanet(Planet):
  def __init__(self, name, radius, population):
    super().__init__(name, radius)
    self.population = population
  def greet(self):
    print("Population of planet {} is {}".format(self.name, self.population))

class RockPlanet(Planet):
  def __init__(self, name, radius, rock_type):
    super().__init__(name, radius)
    self.rock_type = rock_type

planet1 = LivingPlanet("Earth", 6371, 7800000000)
planet2 = LivingPlanet("Utopia", 32123, 9999999999)
planet3 = RockPlanet("Buliga", 6666, "obsidian")
planet1.introduce()
planet2.introduce()
planet3.introduce()
planet1.greet()
planet2.greet()

##Well done - 10/10