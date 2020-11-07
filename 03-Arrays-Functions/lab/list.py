a = ["USA", "Russia", "China", "Azerbaijan", "Portugal", "Germany", "Netherlands", "Turkey"]
print(a[0], a[2])
a[4] = "Spain"
print(a)
for cou in a:
  print(cou[0])
b = [330, 150, 1400,10, 50, 100]
#len(a)
#range(6)
#USA - 330 millions
#i =0...5
#len(b) = 6
#i < len(b), 0...5 < 6
#i >= len(b), b[6] -> print no number
loop = min(len(a), len(b))
#len(a) = 8
#len(b) = 6
#min(len(a), len(b)) = 6
#0...5, b[0],b[1]...b[5]
#0...5, a[0]...a[5]
for i in range(loop):
  #if i < len(b):
  print(a[i] + " - " + str(b[i]))
  #elif i >= len(b):
    #print("There are no population numbers for countries in position : " + str(i-1))
  
#min function, it accepts two numbers, it returns the smallest one
#min(4,6) -> 4
#len(a) - 8
#len(b) - 6

#append - function
#a.append("Kongo")
a.append("Japan")
b.append(500)
print(a)
print(b)

#pop - function
#a.pop(0)
a.pop(0)
a.pop(1)
a.pop(2)
print(a)

#remove - function
#a.remove("USA")
a.remove("Germany")
a.remove("Japan")
print(a)