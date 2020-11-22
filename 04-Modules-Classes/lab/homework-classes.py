class Converter:
  def __init__(self, value):
    self.value = value
  def miles_to_km(self):
    km = self.value * 1.6
    print("{} miles is {} kilometers".format(self.value, km))
  def km_to_miles(self):
    miles = self.value / 1.6
    print("{} kilometers is {} miles".format(self.value, miles))
  def feet_to_meters(self):
    meters = self.value * 0.3048
    print("{} feet is {} meters".format(self.value, meters))

convertion = int(input("1) miles to kilometers\n2)kilometers to miles\n3)feet to meters\nEnter the number of convertion : "))
value = float(input("Enter the value that you want to convert : "))
new_convertion = Converter(value)
if convertion == 1:
  new_convertion.miles_to_km()
elif convertion == 2:
  new_convertion.km_to_miles()
elif convertion == 3:
  new_convertion.feet_to_meters()
  
#Well done, 9/10