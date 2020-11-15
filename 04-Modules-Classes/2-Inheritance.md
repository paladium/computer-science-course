# Inheritance in OOP
Inheritance allows us to define a class that inherits all the methods and properties from another class.

**Parent class** is the class being inherited from, also called base class.

**Child class** is the class that inherits from another class, also called derived class.

## Python inheritance
```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

y = Student("Mike", "Olsen")
y.printname()

```

## Init function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class.

```python
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    #add properties etc.
    self.graduationYear = 2019
x = Student("Mike", "Olsen", 2019)
print(x.graduationYear)
```

> Homework: create a class Transport that has a name, top_speed variables. Create two child classes - Car and Airplane that extend from that class. Add additional variable to Car class - type of engine (diesel, v, flat etc.) and another variable to class Airplane - max altitude. Create 2 objects of type car and aircraft and print all their properties.

> Homework: create a class Planet that has a name, radius variables, it should also have a function named ```introduce```, which will simply print the planet's name and radius (in km). Create another class - LivingPlanet that extends from Planet class, which has a variable - population. Make a new function: ```greet```, which will print the population of the planet. Finally, make a new class RockPlanet, which has another variable - rock_type. Create 3 objects: 2 living planet and 1 rock and call the function ```introduce```(on all 3 objects) and ```greet```(only for LivingPlanet).