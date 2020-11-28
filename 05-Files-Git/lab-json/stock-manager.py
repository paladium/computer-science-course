#Load the stocks.json file
#Ask the user for a new item to add: name, price, availableStock, description
#Append that dict to the list
#Use the dump function to write the result to the same file
import json
stocks = []
with open("stock.json") as file:
  stocks = json.load(file)
  
name = input("Enter the name of the item : ")
price = float(input("Enter the price of the item : "))
availableStock = input("Enter the available stock of the item : ")
description = input("Enter the description of the item : ")
dictionary = {"item" : name, "price" : price, "availableStock" : availableStock, "description" : description}
stocks.append(dictionary)

with open("stock.json", "w") as file:
  json.dump(stocks, file, indent=4)