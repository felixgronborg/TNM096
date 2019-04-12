import heapq
import numpy as np

class Board:
    state = []
    h = -1
    def __init__(self, puzzle, h):
        self.puzzle = puzzle
        self.h = h
    def getPuzzle(self):
        return self.puzzle
    def getH(self):
        return self.h

def index_2d(value, data):
    for i, e in enumerate(data):
        try:
            return i, e.index(value)

        except ValueError:
            pass
    raise ValueError("{} is not in the puzzle.".format(repr(value)))

def manhattan(index1, index2):
    return abs(index1[0] - index2[0]) + abs(index1[1] - index2[1])

def h2(puzzle, goal):
    counter = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            index2 = index_2d(puzzle[i][j], goal)
            counter = counter + manhattan((i,j), index2)
    return counter

def h1(puzzle, goal):
    counter = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if(puzzle[i][j] != goal[i][j]):
                counter += 1
    return counter

def matrixify(theList):
    matrix = []
    for i in range(0, len(theList), 3):
        row = []
        for j in range(0, 3):
            row.append(theList[i + j])
        matrix.append(row)
    return matrix

def findChildren(puzzle):
    #Find index of 0
    newPuzzle = puzzle
    zeroPos = index_2d(0, puzzle)
    #Figure out what moves can be made
    lsitOfChildren = []

    #Check if 0 can move up 
    if(zeroPos[0] > 0):
        print("Can move up to:")
        newPos = [zeroPos[0] - 1, zeroPos[1]]
        newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
        newPuzzle[newPos[0]][newPos[1]] = 0
        print("\n", newPuzzle[0], "\n", newPuzzle[1], "\n", newPuzzle[2])
        lsitOfChildren.append(newPuzzle)
        newPuzzle = puzzle

    #Check if 0 can move down
    if(zeroPos[0] < 2):
        print("Can move down to:")
        newPos = [zeroPos[0] + 1, zeroPos[1]]
        newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
        newPuzzle[newPos[0]][newPos[1]] = 0
        print("\n", newPuzzle[0], "\n", newPuzzle[1], "\n", newPuzzle[2])
        lsitOfChildren.append(newPuzzle)
        print("\n", puzzle[0], "\n", puzzle[1], "\n", puzzle[2])
        newPuzzle = puzzle
    
    #Check if 0 can move left
    if(zeroPos[1] > 0):
        print("Can move left to:")
        newPos = [zeroPos[0], zeroPos[1] - 1]
        newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
        newPuzzle[newPos[0]][newPos[1]] = 0
        print("\n", newPuzzle[0], "\n", newPuzzle[1], "\n", newPuzzle[2])
        lsitOfChildren.append(newPuzzle)
        newPuzzle = puzzle

    #Check if 0 can move right
    if(zeroPos[1] < 2):
        print("Can move right to:")
        newPos = [zeroPos[0], zeroPos[1] + 1]
        newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
        newPuzzle[newPos[0]][newPos[1]] = 0
        print("\n", newPuzzle[0], "\n", newPuzzle[1], "\n", newPuzzle[2])
        lsitOfChildren.append(newPuzzle)
        newPuzzle = puzzle

    #Make moves and save them and calculate heuristics of children
    return


# MAIN ----------------------------------------------------
aPuzzle = [1, 0, 5, 4, 3, 2, 6, 8, 7]
aGoal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Assumes user enters 0-8
#while True:
#    input1 = input("Enter your 8 puzzle: \n")
#    current = [int(s) for s in input1.split()]
#    if(len(current) == 9):
#        break
#while True:
#    input1 = input("Enter the goal puzzle: \n")
#    theGoal = [int(s) for s in input1.split()]
#    if(len(theGoal) == 9):
#        break

start = matrixify(aPuzzle)
thegoal = matrixify(aGoal)

print("\n", start[0], "\n", start[1], "\n", start[2])
print("\n", thegoal[0], "\n", thegoal[1], "\n", thegoal[2])
print("\n", "H1 =", h1(start, thegoal), "\n", "H2 =", h2(start, thegoal))

opened = []
closed = []

current = Board(start, h1(start, thegoal))

opened.append(current)

notries = 0

#Where the magic happens
while(current.getH != 0):
    #Increment number of tries to reach goal
    notries = notries + 1
    #Find children
    findChildren(current.getPuzzle())
    #Move the current puzzle to closed
    closed.append(current)
    opened.remove(current)
    #Add children to open list
    #Sort open list in ascending H order
    #Set first board in open as current and repeat until current H = 0
    break