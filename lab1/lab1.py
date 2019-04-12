from itertools import filterfalse
import copy
#FUNCTIONS ----------------------------------------------------
def index_2d(value, puzzle):
    for i, e in enumerate(puzzle):
        try:
            return i, e.index(value)

        except ValueError:
            pass
    raise ValueError("{} is not in the puzzle.".format(repr(value)))

def manhattan(index1, index2):
    return abs(index1[0] - index2[0]) + abs(index1[1] - index2[1])

#Checks if a puzzle is solveable before doing the search by counting inversions
#Dont work for my code
def solveable(initial):
    
    inv_sum = 0
    for i in range(0, 7):
        for j in range(i+1, 8):
            
            if(initial[j] > 0 and initial[i] > 0 and initial[i] > initial[j]):
                inv_sum += 1

    print("inv_sum: ", inv_sum)
    if(inv_sum % 2 == 0):
        return True
    return False
#CLASSES ----------------------------------------------------
class Board:
    h = -1 
    puzzle = []
    depth = -1
    cost = -1
    def setH(self, puzzle, goal):
        one = True #Change for other heuristics
        counter = 0
        if(one):
            for i in range(len(puzzle)):
                for j in range(len(puzzle[i])):
                    if(puzzle[i][j] != goal[i][j] and puzzle[i][j] != 0):
                        counter += 1
        #oneOrTwo = 2 #TA BORT! TESTAR BARA VAD SOM HÄNDER OM MAN ANVÄNDER BÅDA
        if(not one):
            for i in range(len(puzzle)):
                for j in range(len(puzzle[i])):
                    if(puzzle[i][j] != 0):
                        index2 = index_2d(puzzle[i][j], goal)
                        counter += manhattan((i,j), index2)
        return counter
    
    def setCost(self, path, h):
        return path + h

    def getPuzzle(self):
        return self.puzzle

    def getH(self):
        return self.h

    def getDepth(self):
        return self.depth

    def getCost(self):
        return self.cost

    def generateChildren(self):
        newPuzzle = copy.deepcopy(self.getPuzzle())
        zeroPos = index_2d(0, newPuzzle)
        listOfChildren = []

        #If 0 can move up 
        if(zeroPos[0] > 0):
            newPos = [zeroPos[0] - 1, zeroPos[1]]
            newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
            newPuzzle[newPos[0]][newPos[1]] = 0
            listOfChildren.append(newPuzzle)
            newPuzzle = copy.deepcopy(self.getPuzzle())

        #If 0 can move down
        if(zeroPos[0] < 2):
            newPos = [zeroPos[0] + 1, zeroPos[1]]
            newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
            newPuzzle[newPos[0]][newPos[1]] = 0
            listOfChildren.append(newPuzzle)
            newPuzzle = copy.deepcopy(self.getPuzzle())
        
        #If 0 can move left
        if(zeroPos[1] > 0):
            newPos = [zeroPos[0], zeroPos[1] - 1]
            newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
            newPuzzle[newPos[0]][newPos[1]] = 0
            listOfChildren.append(newPuzzle)
            newPuzzle = copy.deepcopy(self.getPuzzle())

        #If 0 can move right
        if(zeroPos[1] < 2):
            newPos = [zeroPos[0], zeroPos[1] + 1]
            newPuzzle[zeroPos[0]][zeroPos[1]] = newPuzzle[newPos[0]][newPos[1]]
            newPuzzle[newPos[0]][newPos[1]] = 0
            listOfChildren.append(newPuzzle)
            newPuzzle = copy.deepcopy(self.getPuzzle())
        
        return listOfChildren
                    

    #@staticmethod
    def __init__(self, puzzle, goal, depth):
        self.puzzle = puzzle
        self.depth = depth
        self.h = self.setH(puzzle, goal)
        self.cost = self.setCost(depth, self.h)



# MAIN ----------------------------------------------------
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
#start = matrixify(aPuzzle)
#thegoal = matrixify(aGoal)
#test [[1, 2, 3], [8, 6, 4], [7, 5, 0]]
#ezst [[1, 2, 3], [4, 8, 5], [0, 7, 6]]
#easy [[1, 3, 4], [8, 6, 2], [7, 0, 5]]
#medi [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
#hard [[5, 6, 7], [4, 0, 8], [3, 2, 1]]
start = [[1, 3, 4], [8, 6, 2], [7, 0, 5]]
theGoal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#goalBoard = Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]], theGoal)
current = Board(start, theGoal, 0)

opened = []
closed = []

opened.append(current)
limit = 400000000
counter = 0
while(current.getH() != 0):
    #print("\n", current.getPuzzle()[0], "\n", current.getPuzzle()[1],"\n", current.getPuzzle()[2])
    #print("Heuristic h =", current.getH())
    #print("Cost =", current.getCost())

    closed.append(current)
    childPuzzles = current.generateChildren()
    #print("Current board has", len(childPuzzles), "children.")

    for i in range(0, len(childPuzzles)):
        equal = False
        for j in range(0, len(closed)):
            if(childPuzzles[i] == closed[j].getPuzzle()):
                equal = True
        if(not equal):
            opened.append(Board(childPuzzles[i], theGoal, current.getDepth() + 1))
    #print("---------------------------------")
    #print("\n", current.getPuzzle()[0], "\n", current.getPuzzle()[1], "\n", current.getPuzzle()[2])
    #print("---------------------------------")
    print("Depth:", current.getDepth())
    del opened[0]
    opened.sort(key=lambda x: x.cost, reverse = False)
    
    #print("OPEN BOARDS: ")
    #for i in range(0, len(opened)):
        #print("\n", opened[i].getPuzzle()[0], "\n", opened[i].getPuzzle()[1], "\n", opened[i].getPuzzle()[2], "H:", opened[i].getH(), "D:", opened[i].getDepth(), "C:", opened[i].getCost())
    
    current = opened[0]
    
    counter += 1
    if(counter >= limit):
        break
    print("Iterations:", counter)
if(current.getH() == 0):
    print("Solution found in", current.getDepth, "moves:","\n", current.getPuzzle()[0], "\n", current.getPuzzle()[1], "\n", current.getPuzzle()[2])
else:
    print("Last puzzle:\n", current.getPuzzle()[0], "\n", current.getPuzzle()[1], "\n", current.getPuzzle()[2])
