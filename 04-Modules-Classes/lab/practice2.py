from practice import Human
function = int(input("Function : "))
if function == 1: 
  p1 = Human("Alex", 165, 70, "European")
  p2 = Human("Lee", 175, 68, "Asian")
  p3 = Human("Caba", 180, 81, "African")
  p4 = Human("Avonaco", 185, 90, "Native_American")
  p5 = Human("Sarah", 170, 65, "Oceanian")
  persons = [p1, p2, p3, p4, p5]
  for person in persons:
    print(person.name)
    print(person.height)
    print(person.weight)
    print(person.race)
    print("::::::::::::::::::::")
elif function == 2:
  number = int(input("How many humans do you want to create : "))
  persons = []
  for i in range(1, number+1):
    name = input("Enter name : ")
    height = int(input("Enter height : "))
    weight = int(input("Enter weight : "))
    race = input("Enter race : ")
    person = Human(name, height, weight, race)
    persons.append(person)
  print(persons)
  for ind in persons:
    print(ind.name)
    print(ind.height)
    print(ind.weight)
    print(ind.race)
    print("::::::::::::::::::::")

#Good work