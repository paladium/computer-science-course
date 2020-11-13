# Modules
Modules are used to separate common logic into reusable parts. Modules are essentially python files that contain variables, functions and classes.

# Using modules
To make a new module, just make a python file. The name of the fille will be your module name.
For example, let's make a file named calculator.py
```python
def add(a, b):
    return a + b
```

Now if we want to use that function:
```python
import calculator
calculator.add(4, 5)
```

We can also include individual functions from the module:
```python
from calculator import add
add(4, 5)
```

## Variables in modules
We can use variables in module:
Let's make a file named math.py
```python
pi = 3.14567
```
Then we can use:
```python
import math
print(math.pi)
```

## Renaming a module
We can also rename the module to avoid collisions:

```python
import math as super_math
print(super_math.pi)
```

## Built-in modules
There are many modules included in Python language. Some of them are:
- binascii - Tools for converting between binary and various ASCII-encoded binary representations.
- calendar - Functions for working with calendars, including some emulation of the Unix cal program.
- datetime - Basic date and time types.
- email - Package supporting the parsing, manipulating, and generating email messages.
- html - Helpers for manipulating HTML.
- json - Encode and decode the JSON format.
- math - Mathematical functions (sin() etc.).
- os - Various OS-functions (e.g files)
- random - Generate pseudo-random numbers with various common distributions.

## Third-party modules
There are many many more modules (packages) available from other people, in order to use them, we will learn about pip package manager.