# Dictionaries

Dictionaries are similar to lists, but instead of having an index, they have a key.

## Python dict
To make a new dictionary in python, we do the following:
```python
d = {
    "name": "Rover 2",
    "topSpeed": 10,
    "maxDistance": 500
}
```
We can now access the items of that dictionary:
```python
print(d["name"]) -> "Rover 2"
print(d.get("topSpeed")) -> 10
```
We can also change the values:
```python
d["topSpeed"] = 15
d["maxDistance"] = 400
```
We can loop through a dictionary:
```python
for key in d:
    print(key, d[key])
```
Before accessing the item, we can check if the key exists:
```python
if "name" in d:
    print(d["name"])
```
If we want to add a new item, we simply do the following:
```python
d["color"] = "red"
```
Finally, if we want to remove an item:
```python
d.pop("color")
```