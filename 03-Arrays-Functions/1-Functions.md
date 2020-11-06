# Functions

![Function](./img/function.png)

Functions are a reusable piece of code that can work with different values given to it.

Functions can be used to perform common tasks in our application, do mathematical calculations or simply be in place to simplify our code.

## How functions work

Each function has a name (has to be unique) and a number of parameters. Think of parameters as variables to that function.

When you want to use that function - you call it with the same number of arguments that it is defined.

## Python functions
Let's see how python functions work. When you want to define a new function you write the following:
```python
def my_func():
    # do something
```

If you want to pass some arguments:
```python
def my_func(a,b):
    a += b
```

Finally, if you want to return something (means the function will calculate a result and you want to use that result):
```python
def my_func(a, b):
    return a + b
```

And we want to call that function, we do the following:
```python
my_func(1, 2)
```

You can use a different way in Python to call a function with arguments:
```python
my_func(a=1, b=2)
```
These are called named parameters, it is useful if you have complicated function with many inputs.

Python function arguments can have default values:
```python
def my_func(b, a = 1):
    return a + b

my_func(b=3)
my_func(5)
```
As you can see, we didn't specify the value for a, so it takes the default value. But remember, if you call a function without named arguments and it has default parameters, those have to be at the end of function definition.

> Homework: write a function that will calculate the average value in a list

> Homework: write a function to calculate a factorial of a number

> Homework: write a function that takes a string and prints how many uppercase and lowercase characters there are.

> Homework: write a function to print even (divisible by 2) numbers in a list

> Homework: write a function to return all the even numbers between a and b(both given from the user).