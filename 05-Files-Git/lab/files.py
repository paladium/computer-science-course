file = open("test.txt")
data = file.read()
print(data)
file.close()

#With keyword
with open("test.txt") as file:
    data = file.read()
    print(data)

l = []

with open("lines.txt") as file:
    for x in file:
        print(x.strip())
        l.append(x.strip())
print(l)

