# Pip system

Pip system allows you to install packages (modules) made by other people, so that you don't have to write them from scratch (https://pypi.org/).

When you want to install a specific package to your project, you should first create the file - requirements.txt, which basically list all the dependecies that your project requires.

After you make that file, you can list which packages you need in your project:
```txt
Django
```
We only want to install Django web framework, so that we can make servers and websites.

After you list your dependecies, you can run the following command to install them:
```bash
pip install -r requirements.txt
```

We can then use this package in our code (look for examples in documentation of the package):
```python
import django
```

If we want to remove a specific package, just remove it from requirements.txt.