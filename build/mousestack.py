"""
Name: Ryan Bailis
CSCI204 Project 2 Phase 2
Due: Oct. 22, 2018
"""
from build.pyliststack import *

class Mouse:
    def __init__(self):
        pass

        
    def findMazePaths(self, maze, curRow, curCol, endRow, endCol):
        """
        Use a stack to a possible paths in the maze. Takes in a maze, \
        current row/col, and exit row/col. Follows the algorithm given to us.
        """
        #create lists containing curRow and curCol as well as endRow and endCol
        curPos = [curRow,curCol]
        endPos = [endRow,endCol]
        stack = Stack()
        stack.push(curPos)
        while len(stack) != 0:
            curPos = stack.pop()
            if curPos == endPos:
                maze.setValue(curPos[0],curPos[1],maze.THEWAYOUT)
                print("Success")
                print(maze)
                break
            else:
                maze.setValue(curPos[0],curPos[1],maze.THEWAYOUT) #set the value
                if maze.isInMaze(curPos[0]-1,curPos[1]) and maze.isClear(curPos[0]-1,curPos[1]): #check up
                    stack.push([curPos[0]-1,curPos[1]])
                if maze.isInMaze(curPos[0]+1,curPos[1]) and maze.isClear(curPos[0]+1,curPos[1]): #check down
                    stack.push([curPos[0]+1,curPos[1]])
                if maze.isInMaze(curPos[0],curPos[1]-1) and maze.isClear(curPos[0],curPos[1]-1): #check left
                    stack.push([curPos[0],curPos[1]-1])
                if maze.isInMaze(curPos[0],curPos[1]+1) and maze.isClear(curPos[0],curPos[1]+1): #check right
                    stack.push([curPos[0],curPos[1]+1])
                    


                
                

        
