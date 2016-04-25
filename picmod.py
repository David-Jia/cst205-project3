import numpy as np
import random
import cv2
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image
import PIL.ImageOps


# Mods the image based on inputed values
#

def newPixelVal( oldpixel, modifier, negative)
	if(!negative)
		if(oldpixel + modifier > 255)
			return oldpixel + modifier - 255
	else
		if(oldpixel - modifier < 0)
			return oldpixel - modifier + 255

def modfile(filename, redval, greenval, blueval, negative, reverse):
	image = Image.open(filename)
	width, height = im.size(image)
	result_image = makeEmptyPicture(width,height)
	if(reverse)
		for w in range(0, width)
			for h in range(0, height)
				imgpixel = getPixel(image, w, h)
				setRed(getPixel(result_image, w, h), newPixelVal(getRed(imgpixel), redval, true))
				setBlue(getPixel(result_image, w, h), newPixelVal(getBlue(imgpixel), blueval, true))
				setGreen(getPixel(result_image, w, h), newPixelVal(getGreen(imgpixel), greenval, true))
	else 		#not reverse
		for w in range(0, width)
			for h in range(0, height)
				imgpixel = getPixel(image, w, h)
				setRed(getPixel(result_image, w, h), newPixelVal(getRed(imgpixel), redval, false))
				setBlue(getPixel(result_image, w, h), newPixelVal(getBlue(imgpixel), blueval, false))
				setGreen(getPixel(result_image, w, h), newPixelVal(getGreen(imgpixel), greenval, false))
	if(negative)
		for w in range(0, width)
			for h in range(0, height)
				imgpixel = getPixel(image, w, h)
				setRed(getPixel(result_image, w, h), setRed(255-getRed(imgpixel))
				setBlue(getPixel(result_image, w, h), setBlue(255-getBlue(imgpixel))
				setGreen(getPixel(result_image, w, h), setGreen(255-getGreen(imgpixel))
	result_name = filename + "_mod_" + redval + "_" + greenval + "_" + blueval
	cv2.imwrite(result_name, result_image)		
	cv2.imshow(result_name, result_image)
	cv2.waitKey(0)
    cv2.destroyAllWindows()
