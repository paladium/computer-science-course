# Working with images in Python

Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.

## Show an image
To open and show an image do the following:
```python
from PIL import Image
img = Image.open("img.jpg")
img.show()
```

## Display image info
You can display image format, size and mode:
```python
from PIL import Image
img = Image.open("img.jpg")    
print("Format: {0}\nSize: {1}\nMode: {2}".format(img.format, 
    img.size, img.mode))
```

## Filters
Pillow has a number of filters (just like Photoshop), which you can use to modify the image. The following example blurs the image:
```python
from PIL import Image, ImageFilter
img = Image.open("img.jpg")
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred.png")
```

Other filters available:
- CONTOUR
- DETAIL
- EDGE_ENHANCE
- EMBOSS
- FIND_EDGES
- SHARPEN
- SMOOTH

## Croppping image
You can crop an image using Pillow:
```python
from PIL import Image
img = Image.open("img.jpg")
cropped = img.crop((100, 100, 350, 350))
cropped.save('img_cropped.jpg')
```

## Drawing using Pillow
Pillow has some basic 2D graphics capabilities. ImageDraw module provides simple 2D graphics for Image objects. We can create new images, annotate or retouch existing images, and generate graphics on the fly for web use.

```python
from PIL import Image, ImageDraw

img = Image.new('RGBA', (200, 200), 'white')    
idraw = ImageDraw.Draw(img)

idraw.rectangle((10, 10, 100, 100), fill='blue')
 
img.save('rectangle.png')
```