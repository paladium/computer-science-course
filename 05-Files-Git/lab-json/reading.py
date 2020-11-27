import json
with open("stock.json") as file:
    data = json.load(file)

print(data)
print(data[0]["item"])
#Write a program to find the item with the maximum price
max_item = {}
max_price = 0
for item in data:
  if item["price"] > max_price:
    max_item = item
    max_price = item["price"]
print(max_price, max_item)

#Create a new class
class Item:
  def __init__(self, name, price, available_stock, description):
    self.name = name
    self.price = price
    self.available_stock = available_stock
    self.description = description
  def prop_printer(self):
    print("Name - {}\nPrice - {}\nAvailable stock - {}\nDescription : {}\n----------".format(self.name, self.price, self.available_stock, self.description))

items = []
#Go over each element in a list
#Create a new object of class Item with all the values coming from the current item
#Append the object to the list
for element in data:
  a = Item(element["item"], element["price"], element["availableStock"], element["description"])
  items.append(a)
print(items)
#Go over each item in items and call the function prop_printer
for item in items:
  item.prop_printer()