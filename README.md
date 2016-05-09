#CST205 Spring 2016

Project 3
Group 100

David Jia
Brandon Martinez
Harrison Oglesby

Trello: https://trello.com/b/KL7OL107/team-101-project-3-cst-205
Github: https://github.com/HarrisonOg/cst205-project3

Info:

project.py is the main file that needs to be run by itself.
fileopen.py, game.py, and picmod.py are all individual files that are completely merged together in the main project.py file.

The point of the program is that the user first selects an image. They then play a game where they collect red, green, and blue blocks which represent pixel values. Once the game ends, the number of red, green, and blue blocks that they have picked up is added to the RGB color values of all the pixels in the image that they have selected. If they collected the purple block, this number is subtracted instead. The white block places a negative filter onto the image at the end.

The resulting image is also saved.

How to play the Game:

The arrow keys input the direction and the player continuously moves in that direction until a new direction is inputted or until a boundary is hit. 

The space bar acts as the pause button. In order to unpause the game, the user just needs to input a direction with the arrow keys.
