import cv2
import glob, os

import skimage
from PIL import Image, ImageEnhance
import random
import matplotlib.pyplot as plt
import skimage.exposure as skie
from skimage import io
import numpy as np


def addRandomBrightness(filename, randBrightness):
    # image brightness enhancer
    img = Image.open(filename)
    enhancer = ImageEnhance.Brightness(img)
    im_output = enhancer.enhance(randBrightness)
    im_output.save(filename)
    return im_output

def addContrat(filename, randContrast):
    img = Image.open(filename)
    enhancer = ImageEnhance.Contrast(img)
    factor = randContrast #increase contrast
    im_output = enhancer.enhance(factor)
    im_output.save(filename)


def cropImage(filename):
    # Opens a image in RGB mode
    print('file name')
    print(filename)
    im = Image.open(filename)
    # im.show()
    width, height = im.size
    print(width, height)
    print(width * random.uniform(0.85, 1), height * random.uniform(0.85, 1))
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((0, 0, width * random.uniform(0.85, 1), height * random.uniform(0.85, 1)))
    im1 = im1.resize((width, height))
    im1.save(filename)

def show(img):
    # Display the image.
    fig, (ax1, ax2) = plt.subplots(1, 2,
                                   figsize=(12, 3))

    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.set_axis_off()

    # Display the histogram.
    ax2.hist(img.ravel(), lw=0, bins=256)
    ax2.set_xlim(0, img.max())
    ax2.set_yticks([])

    plt.show()


for filename in glob.glob("rotate_brightness/*.jpg"):
    print(filename)
    print(filename[0:len(filename) - 4])
    tmpName = filename[0:len(filename) - 4]
    img = cv2.imread(filename)
    print(type(img))
    randRotation = random.randint(0, 1)
    randType = random.randint(0, 3)
    randCrop = random.randint(0, 15)
    randBrightness = random.uniform(0.9, 1.10)
    randExposure = random.uniform(0.8, 1.2)
    randContrast = random.uniform(1.0, 1.15)
    if randRotation == 0:
        # horizontal flip
        horizontal_flip = cv2.flip(img, 1)
        cv2.imwrite(tmpName + '_horizontal_flip.jpg', horizontal_flip)
        img = io.imread(tmpName + '_horizontal_flip.jpg')
        io.imsave(tmpName + '_horizontal_flip.jpg', skie.exposure.adjust_sigmoid(img))
        cropImage(tmpName + '_horizontal_flip.jpg')
        addRandomBrightness(tmpName + '_horizontal_flip.jpg', randBrightness)
        addContrat(tmpName + '_horizontal_flip.jpg', randContrast)

    else:
        # vertical flip
        vertical_flip = cv2.flip(img, 0)
        cv2.imwrite(tmpName + '_vertical_flip.jpg', vertical_flip)
        img = io.imread(tmpName + '_vertical_flip.jpg')
        io.imsave(tmpName + '_vertical_flip.jpg', skie.exposure.adjust_sigmoid(img))
        cropImage(tmpName + '_vertical_flip.jpg')
        addRandomBrightness(tmpName + '_vertical_flip.jpg', randBrightness)
        addContrat(tmpName + '_vertical_flip.jpg', randContrast)

    if randType == 0:
        cv2.imwrite(tmpName + '_no_rotate.jpg', img)
        io.imsave(tmpName + '_no_rotate.jpg', skie.exposure.adjust_sigmoid(img))
        img = io.imread(tmpName + '_no_rotate.jpg')
        cropImage(tmpName + '_no_rotate.jpg')
        addRandomBrightness(tmpName + '_no_rotate.jpg',randBrightness)
        addContrat(tmpName + '_no_rotate.jpg', randContrast)

    elif randType == 1:
        img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        io.imsave(tmpName + '_rotate_90.jpg', skie.exposure.adjust_sigmoid(img))
        cv2.imwrite(tmpName + '_rotate_90.jpg', img_rotate_90_clockwise)
        # addRandomBrightness(tmpName + '_rotate_90.jpg',randBrightness)
        img = io.imread(tmpName + '_rotate_90.jpg')
        cropImage(tmpName + '_rotate_90.jpg')
        addRandomBrightness(tmpName + '_rotate_90.jpg', randBrightness)
        addContrat(tmpName + '_rotate_90.jpg', randContrast)

    elif randType == 2:
        img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
        io.imsave(tmpName + '_rotate_180.jpg', skie.exposure.adjust_sigmoid(img))
        cv2.imwrite(tmpName + '_rotate_180.jpg', img_rotate_180)
        # addRandomBrightness(tmpName + '_rotate_180.jpg',randBrightness)
        img = io.imread(tmpName + '_rotate_180.jpg')
        cropImage(tmpName + '_rotate_180.jpg')
        addRandomBrightness(tmpName + '_rotate_180.jpg', randBrightness)
        addContrat(tmpName + '_rotate_180.jpg', randContrast)

    elif randType == 3:
        img_rotate_counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        io.imsave(tmpName + '_rotate_counter.jpg', skie.exposure.adjust_sigmoid(img))
        cv2.imwrite(tmpName + '_rotate_counter.jpg', img_rotate_counter)
        img = io.imread(tmpName + '_rotate_counter.jpg')
        cropImage(tmpName + '_rotate_counter.jpg')
        addRandomBrightness(tmpName + '_rotate_counter.jpg', randBrightness)
        addContrat(tmpName + '_rotate_counter.jpg', randContrast)


    # read the image
    # im = Image.open(filename)
    # # image brightness enhancer
    # enhancer = ImageEnhance.Brightness(im)
    # im_output = enhancer.enhance(random.uniform(0.85, 1.15))
    # im_output.save(tmpName + "_brightness.jpg")

    # # read the image
    # im = Image.open(filename)
    # #image brightness enhancer
    # enhancer = ImageEnhance.Contrast(im)
    # im_output = enhancer.enhance(random.uniform(0.7, 1.2))
    # im_output.save(tmpName+"_contrast.jpg")

    # img2 = plt.imread(filename)
    # show(img2)
    # show(skie.rescale_intensity( img2, in_range=(150, 250), out_range=(0, 250)))
    # io.imsave(tmpName+"_exposure.jpg",skie.rescale_intensity(image=img))
    # io.imsave(tmpName+"_exposure.jpg",skie.rescale_intensity( img, in_range=(0.8, .95), out_range=(0, 1)))
    # io.imsave(tmpName+"_exposure.jpg",skie.exposure.adjust_gamma(img,  2))
