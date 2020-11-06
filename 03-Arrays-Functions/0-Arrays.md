# Arrays
![Pool balls](./img/pool-balls.jpg)

Arrays are used to store similar type of data in one variable.

Each item has a unique index. Usually it starts with zero and goes until n - 1, where n is the length of the array.

## Operations on arrays
- Each array element could be accessed and modified. 
- New elements could be added or removed

## Python example of arrays
In python arrays are called lists. 

To make a new list we do the following:
```python
a = []
```
That way we initialise an empty array.
If we want to create a list of strings:
```python
a = ["car", "plane", "helicopter"]
```

To access the first element:
```python
a[0]
```

Change an element
```python
a[0] = "bicycle"
```

Loop through each element:
```python
for item in a:
    print(item)
```

The length of the list:
```python
len(a)
```

Add items:
```python
a.append("rocket")
```

Remove an element:
```python
a.pop(0) #Remove the first element
```

> Homework: write a program that removes duplicates in a list.

> Homework: write a program to combine two lists.

> Homework: write a program to find common elements between two lists.

> Homework: write a program to create a list of all the elements between a and b (a and b is inputted.)

> Homework: find the sum of all the elements in the list.