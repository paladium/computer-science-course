```python
a = 10
b = 50
c = b / a + a / b
if c > 5:
    print("Hello world")
elif c > 5.5:
    print("Hello Earth")
print("Hello Mars")
```

```python
def my_func(n):
    return n * n

n = 10

for i in range(my_func(n)):
    print("Hello world")
```

```python
a = [10, 20, -10, 50, 60, 80, -80]
x = 0
k = 0
for i in range(len(a)):
    if a[i] > x:
        x = a[i]
        k = i
print(a[k])
```

```python
def my_func(a, b):
    x = []
    for i in range(a, b + 1):
        if i % 6 == 0:
            x.append(i)
    return x

print(my_func(10, 30))
```

```python
def my_func(a, b):
    x = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            x.append(i)
    return x

def my_func_2(x):
    for item in x:
        if item % 3 == 0:
            x.remove(item)

x = my_func(10, 20)
my_func_2(x)
print(x)
```

```python
x = [
    {
        "name": "Iphone 11",
        "price": 850,
        "available": True,
    },
    {
        "name": "Samsung A71",
        "price": 500,
        "available": False,
    },
    {
        "name": "Sony Xperia",
        "price": 700,
        "available": False,
    },
    {
        "name": "Huawei 40",
        "price": 890,
        "available": True
    }
]
def my_func(x):
    y = []
    for item in x:
        if item["available"] == True:
            y.append(item)
    return y

y = my_func(x)
print(y)
```

```python
class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time
    def do_task(self):
        print("Doing my task {}, it takes {} min".format(self.name, self.time))

x = [
    Task("Clean house", 40), 
    Task("Throw trash out", 5), 
    Task("Do homework", 10), 
    Task("Walk the dog", 20),
]

for item in x:
    if 10 <= item.time < 20:
        item.do_task()
```

```python
class Animal:
    def __init__(self, name, top_speed):
        self.name = name
        self.top_speed = top_speed
    def walk(self):
        print("Walking at speed {}".format(top_speed))
    def run(self):
        if self.top_speed >= 10:
            print("Running at speed {}".format(top_speed))
        else:
            self.walk()

class Cheetah(Animal):
    pass

class Human(Animal):
    def __init__(self, name, top_speed, nationality)
        super().__init__(name, top_speed)
        self.nationality = nationality
    
b = Human("John", 8, "Azeri")
b.run()
```