import numpy as np
import random
import cv2
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image


# Mods the image based on inputed values
#

def modfile(filename, redval, greenval, blueval):
	image = Image.open(filename)
	width, height = im.size(image)
	result_image = makeEmptyPicture(width,height)
	for w in range(0, width)
		for h in range(0, height)
			imgpixel = getPixel(image, w, h)
			setRed(getPixel(result_image, w, h), getRed(imgpixel) + redval)
			setBlue(getPixel(result_image, w, h), getBlue(imgpixel) + blueval)
			setGreen(getPixel(result_image, w, h), getGreen(imgpixel) + greenval)
	result_name = filename + "_mod_" + redval + "_" + greenval + "_" + blueval
	cv2.imwrite(result_name, result_image)		
	cv2.imshow(result_name, result_image)
	cv2.waitKey(0)
    cv2.destroyAllWindows()
