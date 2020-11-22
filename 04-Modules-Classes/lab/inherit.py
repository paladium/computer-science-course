class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
  def walk(self):
    print("Walking to supermarket")

class Student(Person):
  def __init__(self, fname, lname, major):
    super().__init__(fname, lname)
    #add properties etc.
    self.major = major
  def schedule(self):
    return "My schedule is ...."
x = Student("Mike", "Olsen", "Engineering")
x.printname()
print(x.major)
x.walk()
print(x.schedule())
#print(x.graduationYear)
