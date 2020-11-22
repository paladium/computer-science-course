#Make a new dict
d = {}
print(d)

#Dict with values
a = {
  "name": "Javid",
  "age": 16,
  "position": "Developer",
 # "weight": 80
}
print(a)
print(a["name"])
print(a.get("age"))
print(a.get("height", 180))

#Assigning values
a["name"] = "Ilkin"
a["age"] = 22
print(a)

for key in a:
  print(key, a[key])
key = "weight"
if key in a:
  print(a["weight"])

#Add a new key to the dict:
a["salary"] = 15000
print(a)

a.pop("name")
a.pop("age")
print(a)