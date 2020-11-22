#Employee automation
#AI Jarvis
#Inputs to get from the terminal - name, years of expirience, position.

#Make a function that accepts the name of the employee and his work expierience (in years) and if the number of years is greater than 3, he gets a promotion
#Hello, |Javid, your work expierience is 2 years. No promotion for you for now.
#Hello, Javid, your work exppirience is 4 years. You get promoted to a CEO.
name = input("Your name - ")
experience = int(input("Your experience in years - "))
position = input("Your position in the company - ")
def promoter(name, experience):
  if experience > 3:
    print("Congratulations , {} ! You are promoted to the CEO .".format(name))
  else:
    print("Sorry , {} . You do not have enough experience for being CEO .".format(name))
promoter(name, experience)

#Second function - yearly salary
#It accepts your work experience, if it is 0-3 years - 50 000 $, 3-6 - 70 000 $, > 6 - 100 000$. Return the salary.
def salary_increaser(experience):
  if experience > 6:
    return 100000
  elif 3 <= experience <= 6:
    return 70000
  else:
    return 50000
salary = salary_increaser(experience)
print(str(salary) + "$")
#Third function - return the department and room you going to work in. It accepts your position - Developer, Analytic, Marketer, Seller. Developer -> return "IT department, room 101".
def work_place(position):
  if position == "Developer":
    return "IT department, room 101"
  elif position == "Analytic":
    return "IT department, room 28"
  elif position == "Marketer":
    return "Marketing department, 666"
  elif position == "Seller":
    return "Sales department, 001"
dep_room = work_place(position)
print("You are going to work in {} .".format(dep_room))