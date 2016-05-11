# David Jia, Harrison Oglesby, Brandon Martinez
# Look in README for Trello and Github and other relevant information
import random, pygame, sys
import numpy as np
import cv2
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image
import PIL.ImageOps
from pygame.locals import *

FPS = 30
GAMEWIDTH = 800
GAMEHEIGHT = 600
TILESIZE = 40
TILEWIDTH = int(GAMEWIDTH / TILESIZE)
TILEHEIGHT = int(GAMEHEIGHT / TILESIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
DARKORANGE = (255, 140, 0)
PURPLE = (160, 32, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGREY = (160, 160, 160)
LIGHTPURPLE = (204, 153, 255)
BACKGROUNDCOLOR = BLACK
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
	global FPSCLOCK, GAMEWINDOW, BASICFONT, root
	
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
	
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	GAMEWINDOW = pygame.display.set_mode((GAMEWIDTH,GAMEHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
	pygame.display.set_caption('Color Collector')
	while True:
		runGame()



def runGame():

	# Spawns the player at a random spot
	startx = random.randint(0,TILEWIDTH - 1)
	starty = random.randint(0,TILEHEIGHT - 1)
	playerLocation = {'x': startx, 'y': starty}
	
	# Makes sure the player isn't moving
	playerMove = None
	
	# Spawns the negative and reverse pick-up at a random spot
	negativeLocation = {'x': -1, 'y': -1}
	negativeSpawn = 0
	reverseLocation = {'x': -1, 'y': -1}
	reverseSpawn = 0
	
	# Gives the negative and reverse pick up a random spawn rate
	negativeSpawnChance = random.randint(0, 2000)
	reverseSpawnChance = random.randint(0, 2000)
	
	# Keeps track of how many times the user has picked up a certain color 
	numOfRedPickUp = 0
	numOfGreenPickUp = 0
	numOfBluePickUp = 0
	negativeMessage = "Not Obtained"
	reverseMessage = "Not Obtained"
	negative = False
	reverse = False
	
	# Amount of time the game lasts
	time = 2500
	
	# Assigns all the color pick-ups a random spawn
	redPickUp1 = getRandomLocation()
	redPickUp2 = getRandomLocation()
	redPickUp3 = getRandomLocation()
	redPickUp4 = getRandomLocation()
	redPickUp5 = getRandomLocation()
	greenPickUp1 = getRandomLocation()
	greenPickUp2 = getRandomLocation()
	greenPickUp3 = getRandomLocation()
	greenPickUp4 = getRandomLocation()
	greenPickUp5 = getRandomLocation()
	bluePickUp1 = getRandomLocation()
	bluePickUp2 = getRandomLocation()
	bluePickUp3 = getRandomLocation()
	bluePickUp4 = getRandomLocation()
	bluePickUp5 = getRandomLocation()
	
	while True:
		# if the game is paused
		if (playerMove != None):
			negativeSpawnChance = random.randint(375, 375)
			reverseSpawnChance = random.randint(375, 375)
	
		keyPressed = False
		
		for event in pygame.event.get():
			if event.type == QUIT:
				stop()
			elif event.type == KEYDOWN:
				keyPressed = True
				if (event.key == K_UP and playerLocation['y'] != 0):
					playerMove = UP
				elif (event.key == K_DOWN and playerLocation['y'] != 14):
					playerMove = DOWN
				elif (event.key == K_LEFT and playerLocation['x'] != 0):
					playerMove = LEFT
				elif (event.key == K_RIGHT and playerLocation['x'] != 19):
					playerMove = RIGHT
				# Pause button
				elif (event.key == K_SPACE):
					playerMove = None
		
		# Boundary checks
		if (playerMove == UP and playerLocation['y'] != 0):
			playerLocation = {'x': playerLocation['x'], 'y': playerLocation['y'] - 1}
		elif (playerMove == DOWN and playerLocation['y'] != 14):
			playerLocation = {'x': playerLocation['x'], 'y': playerLocation['y'] + 1}
		elif (playerMove == LEFT and playerLocation['x'] != 0):
			playerLocation = {'x': playerLocation['x'] - 1, 'y': playerLocation['y']}
		elif (playerMove == RIGHT and playerLocation['x'] != 19):
			playerLocation = {'x': playerLocation['x'] + 1, 'y': playerLocation['y']}
			
		# **************************************************************************************************
		# Checks if the player has touched a pick-up	
		if (playerLocation['x'] == redPickUp1['x'] and playerLocation['y'] == redPickUp1['y']):
			redPickUp1 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp2['x'] and playerLocation['y'] == redPickUp2['y']):
			redPickUp2 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp3['x'] and playerLocation['y'] == redPickUp3['y']):
			redPickUp3 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp4['x'] and playerLocation['y'] == redPickUp4['y']):
			redPickUp4 = getRandomLocation()
			numOfRedPickUp += 1
		if (playerLocation['x'] == redPickUp5['x'] and playerLocation['y'] == redPickUp5['y']):
			redPickUp5 = getRandomLocation()
			numOfRedPickUp += 1
			
		if (playerLocation['x'] == bluePickUp1['x'] and playerLocation['y'] == bluePickUp1['y']):
			bluePickUp1 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp2['x'] and playerLocation['y'] == bluePickUp2['y']):
			bluePickUp2 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp3['x'] and playerLocation['y'] == bluePickUp3['y']):
			bluePickUp3 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp4['x'] and playerLocation['y'] == bluePickUp4['y']):
			bluePickUp4 = getRandomLocation()
			numOfBluePickUp += 1
		if (playerLocation['x'] == bluePickUp5['x'] and playerLocation['y'] == bluePickUp5['y']):
			bluePickUp5 = getRandomLocation()
			numOfBluePickUp += 1
			
		if (playerLocation['x'] == greenPickUp1['x'] and playerLocation['y'] == greenPickUp1['y']):
			greenPickUp1 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp2['x'] and playerLocation['y'] == greenPickUp2['y']):
			greenPickUp2 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp3['x'] and playerLocation['y'] == greenPickUp3['y']):
			greenPickUp3 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp4['x'] and playerLocation['y'] == greenPickUp4['y']):
			greenPickUp4 = getRandomLocation()
			numOfGreenPickUp += 1
		if (playerLocation['x'] == greenPickUp5['x'] and playerLocation['y'] == greenPickUp5['y']):
			greenPickUp5 = getRandomLocation()
			numOfGreenPickUp += 1
			
		if (playerLocation['x'] == negativeLocation['x'] and playerLocation['y'] == negativeLocation['y']):
			negativeMessage = "Obtained!"
			negative = True
			removeNegativePickUp(negativeLocation)
			
		if (playerLocation['x'] == reverseLocation['x'] and playerLocation['y'] == reverseLocation['y']):
			reverseMessage = "Obtained!"
			reverse = True
			removeReversePickUp(reverseLocation)
		# **************************************************************************************************
			
		# Draws the player in their new location
		if keyPressed == True:
			drawPlayer(playerLocation)
		
		GAMEWINDOW.fill(BACKGROUNDCOLOR)
		# No longer needed for the final product
		# drawTiles()
		drawPlayer(playerLocation)
		
		# Draws the color pick-ups
		drawRedPickUp(redPickUp1)
		drawRedPickUp(redPickUp2)
		drawRedPickUp(redPickUp3)
		drawRedPickUp(redPickUp4)
		drawRedPickUp(redPickUp5)
		
		drawGreenPickUp(greenPickUp1)
		drawGreenPickUp(greenPickUp2)
		drawGreenPickUp(greenPickUp3)
		drawGreenPickUp(greenPickUp4)
		drawGreenPickUp(greenPickUp5)
		
		drawBluePickUp(bluePickUp1)
		drawBluePickUp(bluePickUp2)
		drawBluePickUp(bluePickUp3)
		drawBluePickUp(bluePickUp4)
		drawBluePickUp(bluePickUp5)
		
		# Spawns the negative and reverse pick-ups if they have not been spawned yet and they have been chosen to 
		# spawn
		if (negativeSpawnChance == 375 and negativeSpawn == 0):
			negativeLocation = getRandomLocation()
			negativeSpawn = 1
			
		if (reverseSpawnChance == 375 and reverseSpawn == 0):
			reverseLocation = getRandomLocation()
			reverseSpawn = 1
			
		if (negativeMessage == "Not Obtained"):
			drawNegativePickUp(negativeLocation)
			
		if (reverseMessage == "Not Obtained"):
			drawReversePickUp(reverseLocation)
		
		# While the game is not paused, decrease the timer
		if (playerMove != None):
			time -= 1
		
		# Information display in the top right corner of the screen
		displayCollection(numOfRedPickUp, numOfGreenPickUp, numOfBluePickUp, time, negativeMessage, reverseMessage)
		
		# Once the time reaches 0, quit the game and modify the image
		if (time == 0):
			pygame.quit()
			modfile(filename, numOfRedPickUp, numOfGreenPickUp, numOfBluePickUp, negative, reverse)
			stop()
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)
					
# Quit the program				
def stop():
	pygame.quit()
	sys.exit()	

# Information display box found in the top right corner of the game
def displayCollection(numOfRedPickUp, numOfGreenPickUp, numOfBluePickUp, time, negativeMessage, reverseMessage):
	collectionBoxRed = BASICFONT.render("Red Pick-Ups: %s" % (numOfRedPickUp), True, WHITE)
	redBoxRect = collectionBoxRed.get_rect()
	redBoxRect.topright = (GAMEWIDTH - 25, 10)
	GAMEWINDOW.blit(collectionBoxRed, redBoxRect)
	
	collectionBoxGreen = BASICFONT.render("Green Pick-Ups: %s" % (numOfGreenPickUp), True, WHITE)
	greenBoxRect = collectionBoxGreen.get_rect()
	greenBoxRect.topright = (GAMEWIDTH - 25, 30)
	GAMEWINDOW.blit(collectionBoxGreen, greenBoxRect)
	
	collectionBoxBlue = BASICFONT.render("Blue Pick-Ups: %s" % (numOfBluePickUp), True, WHITE)
	blueBoxRect = collectionBoxBlue.get_rect()
	blueBoxRect.topright = (GAMEWIDTH - 25, 50)
	GAMEWINDOW.blit(collectionBoxBlue, blueBoxRect)
	
	collectionBoxTime = BASICFONT.render("Time: %s" % (time), True, WHITE)
	timeBoxRect = collectionBoxTime.get_rect()
	timeBoxRect.topright = (GAMEWIDTH - 25, 110)
	GAMEWINDOW.blit(collectionBoxTime, timeBoxRect)
	
	collectionBoxNegative = BASICFONT.render("Negative: %s" % (negativeMessage), True, WHITE)
	negativeBoxRect = collectionBoxNegative.get_rect()
	negativeBoxRect.topright = (GAMEWIDTH - 25, 70)
	GAMEWINDOW.blit(collectionBoxNegative, negativeBoxRect)
	
	collectionBoxReverse = BASICFONT.render("Reverse: %s" % (reverseMessage), True, WHITE)
	reverseBoxRect = collectionBoxReverse.get_rect()
	reverseBoxRect.topright = (GAMEWIDTH - 25, 90)
	GAMEWINDOW.blit(collectionBoxReverse, reverseBoxRect)
	
# Assigns a random x,y coordinate
def getRandomLocation():	
	return {'x': random.randint(0,TILEWIDTH - 1), 'y': random.randint(0,TILEHEIGHT - 1)}

# Draws the red color pick-up at the given location
def drawRedPickUp(redPickUpLocation):
	x = redPickUpLocation['x'] * TILESIZE
	y = redPickUpLocation['y'] * TILESIZE
	redPickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, RED, redPickUpParticle)
	
# Draws the green color pick-up at the given location
def drawGreenPickUp(greenPickUpLocation):
	x = greenPickUpLocation['x'] * TILESIZE
	y = greenPickUpLocation['y'] * TILESIZE
	greenPickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, GREEN, greenPickUpParticle)
	
# Draws the blue color pick-up at the given location
def drawBluePickUp(bluePickUpLocation):
	x = bluePickUpLocation['x'] * TILESIZE
	y = bluePickUpLocation['y'] * TILESIZE
	bluePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, BLUE, bluePickUpParticle)
	
# Draws the Negative pick-up at the given location
def drawNegativePickUp(negativeLocation):
	x = negativeLocation['x'] * TILESIZE
	y = negativeLocation['y'] * TILESIZE
	negativePickUpOuterParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, LIGHTGREY, negativePickUpOuterParticle)
	negativePickUpInnerParticle = pygame.Rect(x + 10, y + 10, TILESIZE - 19, TILESIZE - 19)
	pygame.draw.rect(GAMEWINDOW, WHITE, negativePickUpInnerParticle)
	
# Removes the Negative pick-up by coloring it black
def removeNegativePickUp(negativeLocation):
	x = negativeLocation['x'] * TILESIZE
	y = negativeLocation['y'] * TILESIZE
	negativePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, BLACK, negativePickUpParticle)
	
# Draws the Reverse pick-up at the given location
def drawReversePickUp(reverseLocation):
	x = reverseLocation['x'] * TILESIZE
	y = reverseLocation['y'] * TILESIZE
	reversePickUpOuterParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, PURPLE, reversePickUpOuterParticle)
	reversePickUpInnerParticle = pygame.Rect(x + 10, y + 10, TILESIZE - 19, TILESIZE - 19)
	pygame.draw.rect(GAMEWINDOW, LIGHTPURPLE, reversePickUpInnerParticle)
	
# Removes the Reverse pick-up by coloring it black
def removeReversePickUp(reverseLocation):
	x = reverseLocation['x'] * TILESIZE
	y = reverseLocation['y'] * TILESIZE
	reversePickUpParticle = pygame.Rect(x + 6, y + 6, TILESIZE - 11, TILESIZE - 11)
	pygame.draw.rect(GAMEWINDOW, BLACK, reversePickUpParticle)
	
# Draws the player at the given location
def drawPlayer(playerLocation):
	x = playerLocation['x'] * TILESIZE	
	y = playerLocation['y'] * TILESIZE
	playerOuterShell = pygame.Rect(x + 1, y + 1, TILESIZE - 1, TILESIZE - 1)
	pygame.draw.rect(GAMEWINDOW, DARKORANGE, playerOuterShell)
	playerInnerShell = pygame.Rect(x + 7, y + 7, TILESIZE - 13, TILESIZE - 13)
	pygame.draw.rect(GAMEWINDOW, ORANGE, playerInnerShell)
	
# Divided the game into tiles; No longer needed for the final product
"""def drawTiles():
	for x in range(0, GAMEWIDTH, TILESIZE):
		pygame.draw.line(GAMEWINDOW, WHITE, (x, 0), (x, GAMEHEIGHT))
	for y in range(0, GAMEHEIGHT, TILESIZE):
		pygame.draw.line(GAMEWINDOW, WHITE, (0, y), (GAMEWIDTH, y))"""

# Finds the new pixel value for the given pixel value
def newPixelVal(oldpixel, modifier, reverse):
	if(not reverse):
		if(oldpixel + modifier > 255):
			return oldpixel + modifier - 255
		else:
			return oldpixel + modifier
	else:
		if(oldpixel - modifier < 0):
			return oldpixel - modifier + 255
		else:
			return oldpixel - modifier

# Modifies the image file based on performance in the game
def modfile(filename, redval, greenval, blueval, negative, reverse):
	image = Image.open(filename)		
	width, height = image.size
	result_image = image.copy()
	result_image = result_image.convert('RGB')
	new_Image = Image.new('RGB', (width, height), "black")
	pixels = new_Image.load()
	# If reverse pick-up was collected
	if(reverse):
		for w in range(0, width):
			for h in range(0, height):
				r, g, b = result_image.getpixel((w, h))	
				red = newPixelVal(r, redval, True)
				green = newPixelVal(g, greenval, True)
				blue = newPixelVal(b, blueval, True)
				pixels[w,h] = (red, green, blue)
				
				# If negative pick-up was collected
				if(negative):
					pixels[w,h] = (255 - red, 255 - green, 255 - blue)
			
		imcv = np.array(new_Image)
	
	# If reverse pick-up was not collected			
	else: #not reverse
		for w in range(0, width):
			for h in range(0, height):
				r, g, b = result_image.getpixel((w, h))
				red = newPixelVal(r, redval, False)
				green = newPixelVal(g, greenval, False)
				blue = newPixelVal(b, blueval, False)
				pixels[w,h] = (red, green, blue)
				
				# If negative pick-up was collected
				if(negative):
					pixels[w,h] = (255 - red, 255 - green, 255 - blue)
				
		imcv = np.array(new_Image)
		
	result_name = filename + "_mod_" + str(redval) + "_" + str(greenval) + "_" + str(blueval) + ".jpg"
	cv2.imwrite(result_name, imcv)		
	cv2.imshow(result_name, imcv)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
def openfile():
	global filename
	filename = askopenfilename()
	destroyWindow()
    
def destroyWindow():
	root.destroy()
    
if __name__ == '__main__':
	main() 
