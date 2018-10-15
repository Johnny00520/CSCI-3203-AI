#!bin/env python
import random

def whoGoFirst():
    turn = raw_input("Are you playing Red? (Y/N) \n").upper()
    
    if turn == 'Y':
        return 'Player'
    else:
        return 'Computer'

def getPlayerMove():
    move1, move2 = raw_input("RED move: (with a comma)\n").upper().split(",")
    if move1 not in nodeList or move2 not in nodeList:
        print ("invalid input!")
        getPlayerMove()
    else:
        return move1, move2

def connectMove(move1, move2):
    line.append([move1, move2])
    print line

def isEdgeFree(move1, move2):
    if [move1, move2] not in line and [move2, move1] not in line:
        connectMove(move1, move2)
        return True
    else:
        print ("This move is not valid")
        return False

def getComputerMove():
    randomNode1, randomNode2 = random.sample(xrange(0,7), 2)
    if randomNode1 == 0:
        randomNode1 = 'A'
    if randomNode1 == 1:
        randomNode1 = 'B'
    if randomNode1 == 2:
        randomNode1 = 'C'
    if randomNode1 == 3:
        randomNode1 = 'D'
    if randomNode1 == 4:
        randomNode1 = 'E'
    if randomNode1 == 5:
        randomNode1 = 'F'
    if randomNode1 == 6:
        randomNode1 = 'G'
    if randomNode1 == 7:
        randomNode1 = 'H'
    
    if randomNode2 == 0:
        randomNode2 = 'A' 
    if randomNode2 == 1:
        randomNode2 = 'B' 
    if randomNode2 == 2:
        randomNode2 = 'C' 
    if randomNode2 == 3:
        randomNode2 = 'D' 
    if randomNode2 == 4:
        randomNode2 = 'E' 
    if randomNode2 == 5:
        randomNode2 = 'F' 
    if randomNode2 == 6:
        randomNode2 = 'G' 
    if randomNode2 == 7:
        randomNode2 = 'H' 

    return randomNode1, randomNode2

def isLoser(loserMove1, loserMove2):
    for key1 in line:
        if key1[0] == loserMove1:
            for key2 in line:
                if key2[0] == key1[1]:
                    if key2[1] == loserMove2:
                        return True
                        print (loserMove1, loserMove2)
                    else:
                        return False

def playAgain():
    return raw_input("Play again? (y/n)").lower().startswith('y')
    
# dictionary
nodeList = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7 }

startGame = True
isEdgeSafe = False
line = []
print ("Welcome to the SIM game!")
while True:
    turn = whoGoFirst()
    print (turn + " go first")
    
    while startGame:
        if turn == 'Player':
            playerMove1, playerMove2 = getPlayerMove()
            print ("RED move: " + playerMove1 + playerMove2)
            isEdgeSafe = True

            #check if the edge if free first, then check if the chosen moves 
            # would make userself lose
            if isEdgeFree(playerMove1, playerMove2):
                print "player select right edge"
                if isLoser(playerMove1, playerMove2):
                    print ("Player loses!")
                    startGame = False
                else:
                    turn = 'Computer'
        else:
            #Check if the AI's moves makes AI lose the game first, if not, check
            #if the edge is available. If moves make AI lose, then game over
            computerMove1, computerMove2 = getComputerMove()
            print ("BLUE move: " + computerMove1 + computerMove2)

            if not isLoser(computerMove1, computerMove2): 
                if isEdgeFree(computerMove1, computerMove2):
                    print "Computer select right edge"
                    turn = 'Player'
            elif isLoser(computerMove1, computerMove2):
                print ("Computer loses!")
                startGame = False
            else:
                #This makes AI choose new moves again if the moves it chose makes
                # Ai self lose
                turn = 'Computer'

    if not playAgain():
        break
