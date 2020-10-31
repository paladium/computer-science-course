# There are 3 conditionals keywords in python: if, elif, else
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("The number %d is bigger than number %d" % (a, b))
elif a < b:
    print("The number %d is smaller than number %d" % (a, b))
else:
    print("The number %d is equal to number %d" % (a, b))

