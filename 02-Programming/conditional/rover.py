#Rover example
import time

isStuck = input("Enter yes or no if the rover is stuck: ")
if isStuck == "yes":
    print("The rover is stuck trying to steer back")
    time.sleep(2)
    isStuck = input("Enter yes or no if the rover is still stuck: ")
    if isStuck == "yes":
        print("The rover is still stuck, trying to move left & right")
        time.sleep(3)
        isStuck = input("Enter yes or no if the rover is still stuck: ")
        if isStuck == "yes":
            message = input("Enter message to send to Earth: ")
            print("Sending SOS signal to Earth %s" % message)
        elif isStuck == "no":
            print("The rover has escaped by moving left & right. Continuing the mission")
    elif isStuck == "no":
        print("The rover has escaped by steering back. Continuing the mission")
elif isStuck == "no":
    print("The rover is not stuck. Continuing the mission")
else:
    print("Enter yes or no")