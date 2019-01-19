"""
Name: Ryan Bailis
CSCI204 Project 2 Phase 1
Due: Oct. 15, 2018
"""
from build.mousestack import Mouse
#from mouserecursion import Mouse
from build.maze import Maze

print("Welcome to the Maze program. \n")
maze = Maze()
mouse = Mouse()
while True:
    fName = input( "Enter the number of a pre-generated maze file (1, 2, or 3). Enter 'none' if " \
                + " you want to use a randomly generated maze: ")
    fName = "./build/maze" + fName + ".dat"
    #if the file does not exist, use a randomly generated one
    try:
        if fName != 'none':
            maze.readMaze( fName )
            break
    except FileNotFoundError:
        print("That file can not be found. Try again.")
        continue

print( '-------- The Original Maze --------' )
print( maze )
while True:
    startingRow = int( input( 'Please enter the starting row : ' ) )
    print( startingRow )
    startingCol = int( input( 'Please enter the starting column : ' ) )
    print( startingCol )

    if maze.allowedSpot(startingRow,startingCol) != True:
        print("Starting spot not allowed.")
        continue
    break

while True:
    exitRow = int( input( 'Please enter the exiting row : ' ) )
    print( exitRow )
    exitCol = int( input( 'Please enter the exiting column : ' ) )
    print( exitCol )

    #make sure starting and ending spots are in bounds and are open

    if maze.allowedSpot(exitRow,exitCol) != True:
        print("Exit spot not allowed.")
        continue
    break

#run the mouse through the maze
mouse.findMazePaths( maze, startingRow, startingCol, exitRow, exitCol )


