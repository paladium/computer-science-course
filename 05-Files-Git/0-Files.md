# Files
When storing data for the application, it is inconvinient to have it all in the source of the application. Suppose, we are making an application to predict the price of bitcoin based on the historical data, we will have lots and lots of data and we can update that data every hour. That means, the file with the historical data should be used and our application will load that file and perform nessesary calculations.

## Reading files
Suppose we have a simple test.txt file:

```txt
Hello world
This is awesome
I am a file
```

And if we want to load it into our application, we do the following:

```python
file = open("test.txt")
data = file.read()
print(data)
file.close()
```

This will print all the data loaded from the file. At the end, we should not forget to close the file.

We can simplify this code and let python automatically close the file, when we are done with it:

```python
with open("test.txt") as file:
    data = file.read()
    print(data)
```

## Writing to files

When we want to save our data to a file, we need to do the following:
```python
with open("test.txt", "w") as file:
    file.write("Hello mars as well")
```

As you can see, we need to pass the second parameter to open function, which specifies that we want to write to that file ("w" - write allowed). Since, we are using the with keyword, the file will be written to and closed automatically.

## Go over each line of file
If we want to iterate over each item in a file:
```python
with open("test.txt") as file:
    for x in file:
        print(x)
```

## Append to file
If we already have a file and want to append more data to it, we do the following:

```python
with open("test.txt", "a") as file:
    file.write("Hello I am added")
```

Append will add new lines and keep old ones.

## Deleting files
When we want to delete the file, we do the following:

```python
import os
os.remove("test.txt")
```

## Check if file exists
```python
import os
if os.path.exists("test.txt"):
    #Open the file
else:
    print("File does not exist. Please create one")
```

## Homework - workout app
Make an application to create a simple gym schedule, based on his responses. Ask for information like: name, weight, height, age and goals: Lose Weight, Get Ripped, Prepare for Completition. After getting all the data, prepare three files: lose_weight.txt, get_ripped.txt, prepare_for_competition.txt, which contains day by day instructions what to do (you can find some workouts online). After that, write the result to the file named workout.txt:
```txt
Your measurements:
Name: John
Height: 180cm
Weight: 90kg
Age: 20
--------------
Your workout with the goal of "Lose Weight":
1. Bodyweight Squats—15 reps. Quick tip: Get low, keep your chest up, and don't let your knees go over your toes during this lower-body move.

2. Dumbbell Bench Press—12 reps. Quick tip: Position yourself so your head, back, and butt are all on the bench, your feet flat on the floor.

3. Dumbbell Row—12 reps each side. Quick tip: If you don't have a bench available, try a bent-over row.

4. Lying Isometric Y—Hold for 30 seconds. Quick tip: You can keep your legs on the ground for this one if that feels more comfortable.

5. Box Step-Ups—15 reps each leg. Quick tip: Alternate between your left and right leg, and for an extra challenge, step your lifted foot into a lunge as you come down from the box.

6. Plank—Hold for 30 seconds. Quick tip: Make sure you're keeping your core tight!

```

## Homework - Twitter clone
Make a simple Twitter clone. Ask which command to execute: Get tweets or Write a tweet. When write a tweet is chosen, ask the user for name and tweet content. Then write the result into the file named tweets, which looks like the following:
```txt
Name: John John
Tweet: Today went to the supermarket, forgot the mask, had to come back home 😠
----------------
Name: Elon Musk
Tweet: We are going to Mars 🚀.
```
When user enters Get tweets, read the tweets from the file and print to the user.