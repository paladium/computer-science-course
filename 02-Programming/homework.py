#v=I/nAq

#Three variables to input: I, n, A
#Constant q
#Input floating numbers
#Format the final result
I = float(input("Enter the value of current(I) : "))
n = float(input("Enter the number of free electrons per unit volume(n) : "))
A = float(input("Enter the value of cross sectional area(A) : "))
q = 1.6*10**(-19)
v = I/(n*A*q)
print("The values given :\nI is {0}\nn is {1}\nA is {2}\nThe driving force(v) is equal to {3}".format(I, n, A, v))