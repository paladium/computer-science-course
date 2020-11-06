# We gonna read our city from the terminal - input city
# if the city == Baku then we output happiness
# if our city == London, we output rain
# Otherwise, we output cannot find the city
city = input("Enter the name of a city : ")
if city == "Baku":
  print("Happiness")
elif city == "London":
  print("Rain")
else:
  print("City is not found")