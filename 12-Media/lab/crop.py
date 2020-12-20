from PIL import Image
img = Image.open("baloon.jpg")
cropped = img.crop((752, 173, 1500, 1195))
cropped.save('img_cropped.jpg')