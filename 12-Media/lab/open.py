from PIL import Image
img = Image.open("baloon.jpg")
print("Format: {0}\nSize: {1}\nMode: {2}".format(img.format, 
    img.size, img.mode))
img.show()