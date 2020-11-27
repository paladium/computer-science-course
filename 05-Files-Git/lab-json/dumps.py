import json
x = [
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
        "description": "The new game about a dark future ☮"
    },
    {
        "item": "Xbox series X",
        "price": 609,
        "availableStock": 4564,
        "description": "The new gaming console by Microsoft ",
        "available": True,
        "lastCustomer": None
    }
]

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)