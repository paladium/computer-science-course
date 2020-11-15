# Classes

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Classes are very useful for representing real-world objects and providing an easy way to call functions (their methods) with those objects. For example, we might have a class for airplain, each airplane might have a name, type, it could have a separate function that returns how much time it would take to fly from one place to another specifically for that type of plane.

## Python Classes
To make a new class we use the following construct:
```python
class Aircraft:
    name = "Boeing 747"
```

After making a class (a blueprint), if we want to use that class, we need to make a new object of that class (instantiate that class):
```python
plane = Aircraft()
print(plane.name)
```

## Init function
Init function is a special function that is called when the object of that class is created. You can use that function to set the class variables other operations that are necessary to do when the object is being created:
```python
class Aircraft:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

plane = Aircraft("Boeing 747", 500)
print(plane.name)
print(plane.speed)
```

## Object methods
Objects can also contain methods. Methods in objects are functions that belong to the object:
```python
class Aircraft:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def calculateTime(self, distance):
        return distance / self.speed
plane = Aircraft("Boeing 747", 500)
print("It will take {} hours to fly {} km".format(plane.calculateTime(5000), 5000))
```
The **self** parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

## Change object properties
```python
plane.speed += 100
```

> Homework: write a python class named Converter, which will have 3 functions: convert from miles to km, from km to miles and from feet to meters. Ask user what operation that want to do: miles_to_km, km_to_miles or feet_to_meters, input all values and then run your class's functions to print the result.

> Homework: create a class named Song, which will accept a list of lyrics. The class should also have a function named print_lyrics, which will print the lyrics list one by one.

> Homework: create a python class named Student, which has name and major variables. Make a new function greet which will print the current student's name and major. Make another function named get_schedule, which will return the schedule for the student based on the major (e.g computer science, then Monday, Tuesday, Wednesday, Thursday, Friday 10-6pm).
