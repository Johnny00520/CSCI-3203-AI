#!/bin/bash python
from random import randint


def startPouring(randomNum, randomNum2):
    
    goal = False
    canArray[randomNum]
    print canArray[randomNum]

    canArray[randomNum2] #choose the can 3 or 4
    print canArray[randomNum2]

    #while(goal != True):
    canArray[randomNum] -= canArray[randomNum2]
    if(canArray[randomNum2] == CapacityFive):
        canArray[3] -= canArray[3]
    elif(canArray[randomNum2] == CapacityFour):
        canArray[2] -= canArray[2]
    
    

    print canArray
        
        #if canArray[0] == 40 and canArray[1] == 36 and canArray[2] == 2 and canArray[3] == 2:
        #    goal = True
        #elif canArray[0] == 36 and canArray[1] == 40 and canArray[2] == 2 and canArray[3] == 2:
        #    goal = True
        #else:
        #    goal = False
    
    
    return

MAX_Five = 5
MAX_Four = 4

LeftCan = 40  # array 0
RightCan = 40  # array 1
CapacityFive = 5  # array 2
CapacityFour = 4  # array 3

EmptyFive = 0
EmptyFour = 0

stateCount = 0

canArray = [LeftCan, RightCan, CapacityFive, CapacityFour]
graph = {}

randomNum = randint(0, 1)
randomNum2 = randint(2,3)

print 'first random number is: ', randomNum, ' , second random num is: ', randomNum2

#print startPouring(canArray[randomNum])

startPouring(randomNum, randomNum2)
