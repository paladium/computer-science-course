# Random number generation
Python has a built-in module that you can use to make random numbers.

Return a random number between 0 and 1 (float):
```python
import random
print(random.random())
```
Return a random number between two numbers (int):
```python
import random
print(random.randrange(3, 9))
```
Shuffle a list in random order:
```python
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

```
Return a random item from a list:
```python
import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))

```

> Homework: write a program to generate a random number between 0 and 100 and let user guess it by inputting possible values. At the end print the number of attempts it took.

> Homework: generate a 8-digit random number.

> Homework: return a random character from inputted string.

> Homework: make a game of dice(1-6), where each time user enters "roll" you roll a single dice and you output the result. When the user enters "stop", you stop and calculate total sum.

> Homework: extend a dice game, by allowing user to specify how many dices to play with. For example user enters the number 3, means you need to roll 3 dices and output their results. When the user enters "stop", you stop and calculate total sum of all dices.

> Homework: generate a random password. The length of the password is given from the user. Values you can use: a-z, 0-9.
