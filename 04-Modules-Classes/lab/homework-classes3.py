class Student:
  def __init__(self, name, major):
    self.name = name
    self.major = major
  def greet(self):
    print("Student - {}\nMajor - {}".format(self.name, self.major))
  def get_schedule(self):
    schedules = {"engineering" : "Monday, Wednesday and Friday at 3 pm", "computer science" : "Tuesday, Thursday and Saturday at 3 pm", "business" : "Monday, Wednesday and Friday at 6 pm", "music" : "Tuesday, Thursday and Saturday at 6 pm"}
    if self.major in schedules:
      print("Schedule for student {} : {}".format(self.name, schedules[self.major]))

student1 = Student("Javid", "566")
student1.greet()
student1.get_schedule()

##Well done 10/10. Do not forget to check for key in dict