#Writing to files
with open("test2.txt", "w") as file:
    file.write("Hello mars as well")
    file.write("\nHello Earth")
    l = ["Hello", "world"]
    for x in l:
      file.write("\n" + x)
      file.write("\t\t\t" + x)

#file.write("Doesn't work")