# Install libraries
To install libraries, you would use:
```bash
pip install package_name
```

However, if you want to let other people use your program, you should store your dependecies in a file named ```requirements.txt```:
```txt
flask
Pillow
```
And then if you want to install all dependecies for a project run:
```bash
pip install -r requirements.txt
```