#!bin/env python

import random

ColorList = {'R': 0, 'B': 1, 'O': 2, 'W': 3}
puzzle = ['R', 'R', 'W']

numberColors = 4
numberPostions = len(puzzle)

def check(guess, checkPuzzle):
    rightColor = 0
    #right color and right position
    rightPosition = 0

    # initialize the Matrices all 0
    MatrixPuzzleColor = [0 for i in range(numberColors)]
    MatrixGuessColor = [0 for j in range(numberColors)]

    #print MatrixPuzzleColor

    for e in checkPuzzle:
        MatrixPuzzleColor[e] = MatrixPuzzleColor[e] + 1
        #print ("MatrixPuzzleColor is " + str(MatrixPuzzleColor[e]))

    for f in guess:
        MatrixGuessColor[f] = MatrixGuessColor[f] + 1
        #print ("MatrixGuessColor is " + str(MatrixGuessColor[f]))

    for g in range(len(checkPuzzle)):
        colorCurrent = checkPuzzle[g]
        #print colorCurrent

        if colorCurrent == guess[g]:
            rightPosition = rightPosition + 1

        if MatrixGuessColor[colorCurrent] > 0:
            rightColor + rightColor + 1
            MatrixGuessColor[colorCurrent] = MatrixGuessColor[colorCurrent] - 1
        
        rightColor = rightColor - rightPosition
        if(rightColor < 0):
            rightColor = 0

    return (rightPosition, rightColor)

def guess(guessPuzzle, guessPossibleWays):

    # randomly choose one from the 3D array
    TryGuessing = guessPossibleWays[random.randint(0, len(guessPossibleWays) - 1)]
    #print TryGuessing

    guessX, guessO = check(TryGuessing, guessPuzzle)
    getRidOf = []

    for position in guessPossibleWays:
        checkX, checkO = check(position, TryGuessing)
        # 'or' for string, '|' for number
        if(checkX != guessX) | (checkO != guessO):
            # get rid of any possibility that contains a different answer
            getRidOf.append(position)

    # using remove function to help me
    for i in getRidOf:
        guessPossibleWays.remove(i)

    if (guessX, guessO) == (numberPostions, 0):
        print ("Your answer is: ")
        print (TryGuessing)
    else:
        print (TryGuessing, guessX, guessO)
        guess(guessPuzzle, guessPossibleWays)


print ("===========================================2")


# 3D arrays
possibilities = []
for a in range(numberColors):
    for b in range(numberColors):
        for c in range(numberColors):
            possibilities.append([a, b, c])

puzzle = [random.randint(0, 4), random.randint(0,4), random.randint(0,4)]
print ("Random puzzle is " + str(puzzle))

print ("===========================================1")
guess(puzzle, possibilities)
