#Google maps - find shortest distance between two places
#Names of the places - Iceriseher, Sahil, Narimanov, Nizami
#Your start position - 20 January
#Second list - distance from 20 January (initial position) to all the other places.
#Find shortest path to any place.

#Ask for initial position name: 20 January
#Ask user, enter the number of destinations available: 4
#For each place name and distance from initial position: Sahil, 20
#Icerisehere, 10
#Narimanov, 5

#Ouput destination with the shortest distance from the initial position: Narimanov: 5 km
initial = input("Enter the name of your current place : ")
how_many = int(input("How many places are available to go to : "))
available_places = []
distance = []
for av in range(1, how_many + 1):
  avaiables = input("Enter the name of the {} place where you want to go to : ".format(av))
  available_places.append(avaiables)
  km = float(input("Enter the distance to that place : "))
  distance.append(km)
print(available_places)
print(distance)

#current_smallest = 10**5
#current_index = 0
#go over each element and compare it with the current_smallest, if < current_smallest, change current_index = i, current_smallest = item

current_smallest = 100
current_index = 0
for i in range(len(distance)):
  element = distance[i]
  if element < current_smallest:
    current_smallest = element
    current_index = i
print("The shortest distnace is distnce to {0} , which is {1} km .".format(available_places[current_index], distance[current_index]))