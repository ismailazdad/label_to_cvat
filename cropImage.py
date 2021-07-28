
# Importing Image class from PIL module
import random

from PIL import Image
from resizeimage import resizeimage

# Opens a image in RGB mode
im = Image.open("rotate_brightness/images/test.jpg")
# im.show()
width, height = im.size
print(width, height)
print(width * random.uniform(0.85, 1), height * random.uniform(0.85, 1))
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((0, 0, width * random.uniform(0.85, 1), height * random.uniform(0.85, 1)))
im1 = im1.resize((width, height))

im1.show()


