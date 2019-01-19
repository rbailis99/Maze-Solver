"""
Name: Ryan Bailis
CSCI204 Project 2 Phase 1
Due: Oct. 15, 2018
"""

import random     # random number generator
import copy

class Maze:

    def __init__( self, maxRow = 12, maxCol = 12 ):
        """Create a maze"""
        self.MAXROW = maxRow
        self.MAXCOL = maxCol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '!'

        self.PATH_BLOCKER_RATIO = 0.5

        self.theMaze = self._genMaze()

    def _genMaze( self ):
        """Generate a random maze based on probability"""
        localMaze = [['*' for i in range( self.MAXROW )] \
                         for j in range( self.MAXCOL )]

        for row in range( self.MAXROW ):
            for col in range( self.MAXCOL ):
                threshold = random.random()
                if threshold > self.PATH_BLOCKER_RATIO:
                    localMaze[ row ][ col ] = self.POSSIBLEPATH
                else:
                    localMaze[ row ][ col ] = self.BLOCKER

        return localMaze

    def __str__( self ):
        """Generate a string representation of the maze"""
        string = " "
        for i in range(self.getColSize()):
            i = str(i)[-1]
            string += i
        string += "\n"
        
        rowCounter = 0
        for row in self.theMaze:
            rowCounterStr = str(rowCounter)[-1]
            
            string += rowCounterStr
            for ch in row:
                string += str(ch)
            string += "\n"
            rowCounter += 1
        return string

    def getColSize( self ):
        """Return column count"""
        return len(self.theMaze[0])

    def getROWSize( self ):
        """Return row count"""
        return len(self.theMaze)

    def readMaze( self, fileName ):
        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
        with open(fileName) as f:
            self.theMaze = []
            for line in f:
                row = []
                for ch in line:
                    if ch != "\n":
                        row.append(ch)
                self.theMaze.append(row)
            return self.theMaze

    def getMaze( self ):
        """Return a copy of the maze"""
        return copy.deepcopy(self)

    def isClear( self, row, col ):
        """Determine if this cell is clear (pathway)."""
        return self.getValue(row,col) == self.POSSIBLEPATH

    def isInMaze( self, row, col ):
        """Determine if a cell is inside the maze."""
        return row in range(self.getROWSize()) and col in range(self.getColSize())

    def setValue( self, row, col, value ):
        """Set the value to a cell in the maze."""
        assert self.isInMaze(row,col) , "Not in range of maze"
        self.theMaze[row][col] = value

    def getValue( self, row, col ):
        """Return the value of the current cell."""
        return self.theMaze[row][col]

    def allowedSpot(self, row, col):
        if self.isInMaze(row,col):
            return self.isClear(row,col)
        return False



