import numpy as np
import cv2
import random
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image


def openfile():
    filename = askopenfilename()
    image = cv2.imread(filename)
    result_image = image.copy()
    blurFileName = "./result_" + str(int(random.random() * 1000)) + ".png"
    cv2.imwrite(blurFileName, result_image)
    cv2.imshow(blurFileName, result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = Tk()

# buttons the appear for the GUI
button = Button(text="Choose Image", command=openfile)
button.place(x = 225, y = 200)

# setup the main gui window using Tkinter
width, height = 550, 400
root.minsize(width,height)
root.maxsize(width,height)
im = Image.open("otter.jpg")
tkimage = ImageTk.PhotoImage(im)
myvar = Label(root, image = tkimage)
myvar.place(x=0,y=0,relwidth=1,relheight=1)
myvar.lower()
root.wm_title("File Chooser GUI")
root.mainloop()

