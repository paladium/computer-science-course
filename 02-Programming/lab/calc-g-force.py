#Calculate the g force for two objects with mass m1 and m2 and the distance between their centers - r 

# int - whole number, 0, 1, -1
# float - 5.6, 3.444456
# string - "My name is Ilkin"
#1. Change int variables to float
#2. Print the force like this: The total force is #F#
#3. Add the labels to input the variable
#4. Format the final string like this - My values are: m1 = #m1#, m2 = #m2#, r = #r#, the total force is #F#

G = 6.67*10**(-11)
m1 = float(input("Enter the number : "))
m2 = float(input("Enter the number : "))
r = float(input("Enter the number : "))
F = (G*m1*m2)/r**2

#Format of the string
# The total force is %f
# My paramaters are: m1 = %f, m1 = %f, r = %f,
print("My values are :\nm1 = {0}\nm2 = {1}\nr = {2} \nMy total force is {3}".format(m1, m2, r, F))
#print('The total force is ', F)
#input() function, optional string, it is gonna be displayed when you type, input("Enter the number") -> Enter the number
