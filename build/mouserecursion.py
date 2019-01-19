"""
Name: Ryan Bailis
CSCI204 Project 2 Phase 1
Due: Oct. 15, 2018
"""
class Mouse:
    def __init__(self):
        pass

        
    def findMazePaths(self, maze, curRow, curCol, exitRow, exitCol):
        """
        Use recursion to find all possible paths in the maze. Takes in a maze, \
        current row/col, and exit row/col. 
        """
        new = maze.getMaze()
        new.setValue(curRow,curCol, new.THEWAYOUT)
        
        if curRow == exitRow and curCol == exitCol:
            #base case
            print("Success!")
            print("A path was found:")
            print(new)

        else:
            #recursive step. Move in all directions from current spot and repeat this until we find the exit. 
            if maze.allowedSpot(curRow-1,curCol): #check up
                self.findMazePaths(new, curRow-1, curCol, exitRow, exitCol)

            if maze.allowedSpot(curRow+1,curCol): #check down
                self.findMazePaths(new, curRow+1, curCol, exitRow, exitCol)

            if maze.allowedSpot(curRow,curCol-1): #check left
                self.findMazePaths(new, curRow, curCol-1, exitRow, exitCol)

            if maze.allowedSpot(curRow,curCol+1): #check right
                self.findMazePaths(new, curRow, curCol+1, exitRow, exitCol)


                
                

        
