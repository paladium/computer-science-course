from PIL import Image, ImageFilter
img = Image.open("baloon.jpg")
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred.png")

edges = img.filter(ImageFilter.FIND_EDGES)
edges.save("edges.png")

contour = img.filter(ImageFilter.CONTOUR)
contour.save("contour.png")