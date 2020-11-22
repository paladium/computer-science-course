#Make a class Human
#1st part
#Human can have a name, height, weight and race
#Make 5 humans and print all their properties to the user


#2st part
#Ask user how many humans to create - 4 or 5
#Ask for each humans parameters from the terminal - Enter the name, enter the height etc.
#Make a new human object and store it in the list
#Go over each list item and print each human's name, weight all properties

#Separate that app into two files - two modules
#One module is going to have Human class
#Second module is going to include - import that class and do all the work
class Human:
  def __init__(self, name, height, weight, race):
    self.name = name
    self.height = height
    self.weight = weight
    self.race = race
  def __str__(self):
    return "Name={},Height={},Weight={},Race={}".format(self.name, self.height, self.weight, self.race)