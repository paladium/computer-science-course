#There are two ways to do it repeating actions in python: 
# for loop and whole loop

##For loop
a = int(input("Enter a number of icecreams you want: "))
# range - 0 ... a, a = 5
# 0, 1, 2, 3, 4
for icecream in range(a):
    print("Icecream #%d is ready" % icecream)
