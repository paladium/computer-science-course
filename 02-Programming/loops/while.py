##While loop
wantIcecream = input("Do you want an icecream (yes or no): ")
currentIcecream = 0
while wantIcecream == "yes":
    print("Icecream #%d is ready", currentIcecream)
    currentIcecream += 1
    wantIcecream = input("Do you want an icecream (yes or no): ")
