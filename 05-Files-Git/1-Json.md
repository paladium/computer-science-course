# Json format
When storing data, we would often like to convert it to objects or dictionaries. Making our format is inconvenient and error-prone. Therefore, existing text-based formats exist, which help you to store and work with data.

One of those formats is JSON (JavaScript Object Notation), others exist as well: XML, YAML etc.

JSON file has: string, float, int, arrays, dictionaries (objects), booleans.

Example of the JSON file:
```json
[
    {
        "item": "Playstation 5",
        "price": 566.55,
        "availableStock": 5667,
        "description": "The new gaming console"
    },
    {
        "item": "Nvidia RTX 3090",
        "price": 1010,
        "availableStock": 534,
        "description": "The new powerful GPU by Nvidia"
    },
    {
        "item": "Cyberpunk 2077",
        "price": 60,
        "availableStock": 23434,
        "description": "The new game about a dark future"
    },
    {
        "item": "Xbox series X",
        "price": 609,
        "availableStock": 4564,
        "description": "The new gaming console by Microsoft"
    }
]
```

## Reading JSON
When we want to read the json file in python:

```python
import json
with open("stock.json") as file:
    data = json.load(file)
    print(data)
```

If we are loading the json from the string:
```python
import json
jsonData = '{ "name":"John", "age":30, "city":"New York"}'
data = json.loads(jsonData)
print(data)
```

## Converting to JSON
When we want to convert our dictionary to json:

```python
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

## Writing JSON
When we want to write our json to file:
```python
import json

data = {
    "name": "Test",
    "price": 40404,
    "available": True,
}

with open("output.json", "w") as file:
    json.dump(data, file)
```

## Homework - ecommerce
Make a simple ecommerce application. It should have the following functions: get all items, add an item, delete item, update item price or available stock. All the items, should be stored in a file, named ecommerce.json. Suppose we have the following file:
```json
[
    {
        "item": "Playstation 5",
        "price": 566.55,
        "availableStock": 5667,
        "description": "The new gaming console"
    },
    {
        "item": "Nvidia RTX 3090",
        "price": 1010,
        "availableStock": 534,
        "description": "The new powerful GPU by Nvidia"
    },
    {
        "item": "Cyberpunk 2077",
        "price": 60,
        "availableStock": 23434,
        "description": "The new game about a dark future"
    },
    {
        "item": "Xbox series X",
        "price": 609,
        "availableStock": 4564,
        "description": "The new gaming console by Microsoft"
    }
]
```
When user asks to get all the items, you should print them like this:
```txt
Item: Playstation 5
Price: 566.55
Available Stock: 5667
Description: The new gaming console
-----------------
Item: Nvidia RTX 3090
Price: 1010
Available Stock: 534
Description: The new powerful GPU by Nvidia
...
```
When user wants to add a new item, you ask for item name, price, available stock and description. Then you add the item and let the user know the item was added succesfully.

When user wants to delete the item, you list available options, like this:
```txt
Which item, do you want to delete, enter the item number:
1. Playstation 5
2. Nvidia RTX 3090
3. Cyberpunk 2077
4. Xbox series X
Item to delete : 3
```
If the user enters the item 3, we then proceed to remove the item (Cyberpunk 2077) from our list and do not forget to write the list to the file.

Finally, when the user wants to update item price or available stock, we ask in the same way as we asked for the item to delete:
```txt
Which item's price, do you want to update, enter the item number:
1. Playstation 5
2. Nvidia RTX 3090
3. Cyberpunk 2077
4. Xbox series X
Item to update the price for : 3
New Price: 556.67
```
If the user enters the number 3, you update the third items price and do not forget to write that to file. 

Do the same update, but for the available stock field.

## Homework - Make a simple telegram clone
You should have two files: accounts.json and messages.json. Accounts.json will store the user accounts: username and password and allow the users to register.

Messages.json will store the messages sent from user to user.

When the user runs the application, he should see the following screen:

```txt
Choose what you want to do:
1. Register
2. Login
3. Send a message
4. Get messages
5. Exit
```

### Register
When user chooses the register option, he sees the following screen:
```txt
Enter the username: ilkin-test
Enter the password: secret
```
And after that the user account is saved into the file named accounts.json. Also check whether the user with the same username doesn't exist already.

After the user registers, show the main menu again (continue showing until he enters the 5 - Exit).

### Login
When user chooses the Login, the following screen is presented:
```txt
Enter the username: ilkin-test
Enter the password: secret

Logged in successfully
```
If the username + password, match the data in accounts.json, we allow user to login and show the main menu again.

### Send the message
When user chooses the send message command, he sees the following screen:
```txt
Available recipients:
javid-test
obama
elon-musk
Enter the recipient: elon-musk
Enter the message: Hi, Elon
Your message it sent successfully.
```
After the message is sent, return to the main screen.

### Get messages
When user chooses the get the messages:
```txt
Available senders:
javid-test
obama
elon-musk
Enter the sender: elon-musk
Messages:
you: Hi, Elon
elon-musk: Hi, ilkin
you: How you doing?
elon-musk: Good and you?
```

### Exit
When user enters the exit, the application is exited.

### Notes
The application should be implemented using classes. You will have 5 classes for each available command:

```python
class Login:
    def run(self):
        #Do something
```
Each class will the run function which will be executed when this command is called. It could have other functions as well, like loading user accounts. When functionality is shared, it is a good idea to use inheritance, like for the Login and Register classes, you could make a single parent class named Account:

```python
class Account:
    def getAccounts(self):
        #Load the file and return the accounts

class Login(Account):
    def run(self):
        accounts = self.getAccounts()
        #Do something with accounts
```

When main menu, should also be converted into the class:
```python
class MainMenu:
    def run(self):
        #Print main menu
```
And within the class main menu (__init__ function) create all the nessesary objects (Login, Register, SendMessage etc.).