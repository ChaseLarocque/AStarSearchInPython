"""
Chase Larocque - 1510484
AUCSC 460
Assignment 1 Q.7

This file will solve the 8 puzzle problem using A* search. The cost of each move is 1,
and the huristic is the sum of the manhattan distance.

File contains:

class State
This class is used to represent the state, as well as store the g, f and direction
the blan tile moved from it's parent.

getInput() -> State
This function handles input for the initial state for the 8 puzzle problem
as well as error checking. It then returns the new state.

printPaths(state)
Function takes the goal state, once arrived, and prints it, along with the parent nodes.

calculateManhattanDistance(state) -> manhattanDistance
Function takes a state and calculates the manhattan distance. Function then
returns the manhattan distance.

aStarSearch(initialState)
Function handles the actual a star search, starting with the inital state. Function
also keeps track of the move count.

calculateNewMoves(state) -> newStates
Function calculates the list of possible new moves from the current state. Function
then returns the list of new states.
"""


class State:
    '''Class for storing the state as well as f and g values, parent node and the direction the blank tile moved from the parent'''
    def __init__(self, state, f, g, direction, parent):
        self.state = state
        self.f = f
        self.g = g
        self.direction = direction
        self.parent = parent


def getInput():
    '''This function handles input for the initial state for the 8 puzzle problem as well as error checking. It then returns the new state.'''
    print("Enter 9 Numbers, 3 on each line with a space in between (including 0):")
    testNumbers = {} #dictionary will be used to test for duplicates because of constant access time
    state = [["" for i in range(3)] for j in range(3)] #2d Array

    #grab user input for first row
    while(True):
        line1 = input().strip()
        #Assure numbers are in proper order
        if(len(line1) < 5 or not line1[0].isdigit() or not line1[1] == " " or not line1[2].isdigit() or not line1[3] == " " or not line1[4].isdigit()):
            print("Invalid Line. Please Enter Only 3 Numbers Per Line:")
            continue
        #assure numbers are in range of 0 to 8
        if(eval(line1[0]) > 8 or eval(line1[0]) < 0 or eval(line1[2]) > 8 or eval(line1[2]) < 0 or eval(line1[4]) > 8 or eval(line1[4]) < 0):
            print("Numbers Out Of Range. Please Enter 3 Number Per Line Between 0 and 9 Inclusive:")
            continue
        #check to see if first set of numbers are the same
        if line1[2] == line1[0] or line1[0] == line1[4] or line1[2] == line1[4]:
            print("Repeat Values Not Allowed. Please Reenter Numbers")
            continue
        
        testNumbers[line1[0]] = " "
        testNumbers[line1[2]] = " "
        testNumbers[line1[4]] = " "
        state[0][0] = eval(line1[0])
        state[0][1] = eval(line1[2])
        state[0][2] = eval(line1[4])
        break

    #grab user input for second row
    while(True):
        line2 = input().strip()
        #assure user numbers are in proper order
        if(len(line2) < 5 or not line2[0].isdigit() or not line2[1] == " " or not line2[2].isdigit() or not line2[3] == " " or not line2[4].isdigit()):
            print("Invalid Line. Please Enter Only 3 Numbers Per Line: (Re-enter line 2)")
            continue
        #assure numbers are in proper range
        if(eval(line2[0]) > 8 or eval(line2[0]) < 0 or eval(line2[2]) > 8 or eval(line2[2]) < 0 or eval(line2[4]) > 8 or eval(line2[4]) < 0):
            print("Numbers Out Of Range. Please Enter 3 Number Per Line Between 0 and 9 Inclusive: (Re-enter line 2)")
            continue
        #assure no duplicate numbers
        if(line2[0] in testNumbers or line2[2] in testNumbers or line2[4] in testNumbers):
            print("Repeat Values Not Allowed. Please Reenter Numbers: (Re-enter line 2)")
            continue
        testNumbers[line2[0]] = " "
        testNumbers[line2[2]] = " "
        testNumbers[line2[4]] = " "
        state[1][0] = eval(line2[0])
        state[1][1] = eval(line2[2])
        state[1][2] = eval(line2[4])
        break

    #grab user input for 3 row 
    while(True):
        line3 = input().strip()
        #assure numbers are in proper order
        if(len(line3) < 5 or not line3[0].isdigit() or not line3[1] == " " or not line3[2].isdigit() or not line3[3] == " " or not line3[4].isdigit()):
            print("Invalid Line. Please Enter Only 3 Numbers Per Line: (Re-enter line 3)")
            continue
        #assure numbers in proper range
        if(eval(line3[0]) > 8 or eval(line3[0]) < 0 or eval(line3[2]) > 8 or eval(line3[2]) < 0 or eval(line3[4]) > 8 or eval(line3[4]) < 0):
            print("Numbers Out Of Range. Please Enter 3 Number Per Line Between 0 and 9 Inclusive: (Re-enter line 3)")
            continue
        #assure numbers are not duplicates
        if(line3[0] in testNumbers or line3[2] in testNumbers or line3[4] in testNumbers):
            print("Repeat Values Not Allowed. Please Reenter Numbers: (Re-enter line 3)")
            continue
        state[2][0] = eval(line3[0])
        state[2][1] = eval(line3[2])
        state[2][2] = eval(line3[4])
        newState = State(state, 0, 0, " ", " ") #create root

        #print the new input state
        print("\nOutput:")
        print("Initial")
        for i in range(len(newState.state)):
            for j in range(len(newState.state[i])):
                if newState.state[i][j] == 0: #print 0 as a space
                    print(" ", end = " ") 
                else:
                    print(newState.state[i][j], end = " ")
            print()
        print()
        
        return newState
        
def printPaths(state):
    '''Function takes the goal state, once arrived, and prints it, along with the parent nodes.'''
    pathStates = []
    moveNumber = 0

    #add goal state and all the parents to a list in order to print them 
    while(state.parent != " "):
        pathStates.insert(0, state)
        state = state.parent

    #print the state 
    for state in pathStates:
        moveNumber += 1
        print("Move Number", moveNumber, "(" + state.direction + ")")
        for i in range(len(state.state)):
            for j in range(len(state.state[i])):
                if state.state[i][j] == 0: #print 0 as a space
                    print(" ", end = " ") 
                else:
                    print(state.state[i][j], end = " ")
            print()
        print()

    print("======================================")
    print("     Goal Reached In " + str(moveNumber) + " Moves")
    print("======================================\n")
    print("Enter New Initial State")

def calculateManhattanDistance(state):
    '''Function takes a state and calculates the manhattan distance. Function then returns the manhattan distance.'''
    manhattanDistance = 0
    #tuple in directionary refers to (ycoord, xcoord) if on a cartesian plane
    correctPositions = {0: (0,0), 1: (0,1), 2: (0,2), 
                        3: (1,0), 4: (1,1), 5: (1,2),
                        6: (2,0), 7: (2,1), 8: (2,2)}
    
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                #i correlates to y value on cartesian plane, j correlates to x value on cartesian plane
                manhattanDistance += ((abs(i - correctPositions[state[i][j]][0]) + abs(j - correctPositions[state[i][j]][1])))
                
    return manhattanDistance



def aStarSearch(initialState):
    '''Function handles the actual a star search, starting with the inital state. Function also keeps track of the move count.'''
    from itertools import chain 
    queue = []
    explored = set()
    moveCount = 0
    MAXMOVECOUNT = 100 #Edit this value for more moves
    GOALSTATE = [[0,1,2],[3,4,5],[6,7,8]]

    queue.append(initialState)

    
    while(True):
        #Can't reach goal
        if len(queue) == 0:
            print("~~Failure~~")
            print("Enter New Initial State")
            return

        #Max move count
        if moveCount == MAXMOVECOUNT:
            print("~~Max Moves Performed.~~")
            print("Enter New Initial State")
            return

        poppedState = queue.pop(0)

        if poppedState.state == GOALSTATE:
            printPaths(poppedState)
            return

        moveCount += 1
        
        #i change the nested list to a flat tuple so I can add it to the set (since set items have to be immutable)
        #I use a set to check for explored because it has constant time access.
        explored.add(tuple(list(chain.from_iterable(poppedState.state))))
        newMoves = calculateNewMoves(poppedState)
        
        for state in newMoves:
             #i change the nested list to a flat tuple so I can add it to the set (since set items have to be immutable)
            #I use a set to check for explored because it has constant time access.
            if (tuple(list(chain.from_iterable(state.state))) not in explored):
                itemAdded = False
                #item has not been explored yet. Look to see where it goes in queue
                for i in range(len(queue)):
                    if state.f <= queue[i].f:
                        queue.insert(i, state)
                        itemAdded = True
                        break

                #If we reach the end of the queue without adding the new state, just put it in the queue at end
                if not itemAdded:
                    queue.append(state)
                    
            else: #state has already been explored, check to see if the f value is less in this new path. If it is, replace.
                for i in range(len(queue)):
                    if queue[i].state == state.state and queue[i].f > state.f:
                        queue[i] = state

def calculateNewMoves(state):
    '''Function calculates the list of possible new moves from the current state. Function then returns the list of new states.'''
    newStates = []
    #keep track of where 0 is
    xLoc = 0
    yLoc = 0

    #find 0
    for i in range(len(state.state)):
        for j in range(len(state.state[i])):
            if state.state[i][j] == 0:
                xLoc = j
                yLoc = i
    #can only move blank tile left if we're not at the left boundary
    if xLoc != 0:
        tempState = [x[:] for x in state.state]
        tempState[yLoc][xLoc], tempState[yLoc][xLoc - 1] = tempState[yLoc][xLoc - 1], tempState[yLoc][xLoc]
        newF = state.g + 1 + calculateManhattanDistance(tempState)
        newStates.append(State(tempState, newF, state.g + 1, "Move blank tile left", state))
    #can only move the blank tile right if we're not at the right boundary
    if xLoc < (len(state.state[i]) - 1):
        tempState1 = [x[:] for x in state.state]
        tempState1[yLoc][xLoc], tempState1[yLoc][xLoc + 1] = tempState1[yLoc][xLoc + 1], tempState1[yLoc][xLoc]
        newF2 = state.g + 1 + calculateManhattanDistance(tempState1)
        newStates.append(State(tempState1, newF2, state.g + 1,  "Move blank tile right", state))
    #can only move the blank tile up if we're not at the ceiling
    if yLoc != 0:
        tempState2 = [x[:] for x in state.state]
        tempState2[yLoc][xLoc], tempState2[yLoc - 1][xLoc] = tempState2[yLoc - 1][xLoc], tempState2[yLoc][xLoc]
        newF3 = state.g + 1 + calculateManhattanDistance(tempState2)
        newStates.append(State(tempState2, newF3, state.g + 1, "Move blank tile up", state))
    #can only move the blank tile down if we're not at the floor
    if yLoc < (len(state.state) - 1):
        tempState3 = [x[:] for x in state.state]
        tempState3[yLoc][xLoc], tempState3[yLoc + 1][xLoc] = tempState3[yLoc + 1][xLoc], tempState3[yLoc][xLoc]
        newF4 = state.g + 1 + calculateManhattanDistance(tempState3)
        newStates.append(State(tempState3, newF4, state.g + 1, "Move blank tile down",state))
    return newStates

while(True):
    state = getInput()
    aStarSearch(state)
        
