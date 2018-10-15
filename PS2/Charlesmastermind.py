from random import *

#4 colors, 3 positions
#for ease of code, my colors will be color 0, color 1, color 2 and color 3
puzzle = [0,1,1]

numColors = 4
numPositions=len(puzzle)

def guesser(puzzle, possible):
	print(len(possible))		
	guess = possible[ randint(0,len(possible)-1) ] #pull a random guess
	
	#either get user input, or write a script to check. we need the script anyways
	# for checking all the possibilities against our guess, so might as well use it here as well.
	(gX,gO) = checker(guess,puzzle)
	
	toRemove = []
	for pos in possible:
		(cX, cO) = checker(pos, guess)
		if (cX != gX) | (cO != gO):
			toRemove.append(pos) #remove any possibility that produces a different answer
	
	for r in toRemove:
		possible.remove(r)
	
	if (gX,gO) == (numPositions,0):
		print("the answer is:  ")
		print(guess)
	else:
		print(guess, gX, gO)
		guesser(puzzle, possible)
	
def checker(guess,puzzle):
	#print("checking")
	colorRight = 0
	posRight = 0	#this implies that color is also right
	
	puzzleColorMatrix = [0 for each in range(numColors)]
	guessColorMatrix = [0 for each in range(numColors)]
	
	for p in puzzle:
		puzzleColorMatrix[p] +=1
	
	for g in guess:
		guessColorMatrix[g] +=1
	
	for i in range(len(puzzle)):
		currentColor = puzzle[i]
		
		if currentColor==guess[i]:
			posRight +=1
		
		if guessColorMatrix[currentColor] >0:
			colorRight+=1
			guessColorMatrix[currentColor] -= 1
		colorRight -= posRight
		if (colorRight < 0):
			colorRight =0
			
	return (posRight,colorRight)




##################################
#initial program setup

possibilities = []
for i in range(numColors):
	for j in range(numColors):
		for k in range(numColors):
			possibilities.append([i,j,k])			

#selects a random puzzle for testing
puzzle = [randint(0,numColors),randint(0,numColors),randint(0,numColors)]
print(puzzle)
print("**************************")
guesser(puzzle, possibilities)
