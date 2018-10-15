#Charles Davies


import random

gameSize = 7
#note my game uses points 0-7 instead of A-H
#this would be an easy fix, just print out letters instead of numbers



#con matrix holds the moves. ex move of poit 1 to 4 is stored as conMatrix[1][4] = player1
#really could use a diagonal, as it is mirrored about x==y...

conMatrix = [[" " for x in range(gameSize)] for x in range(gameSize)] #resets conMatrix to empty
turnColor = 0	#resets turn to 0



def showMatrix():
	for each in conMatrix:
		s=''
		for e2 in each:
			s = s + str(e2) + "\t " 
		print(s)

def showGameState():
	p0=[]
	p1=[]
	left = []
	print("----------------------")
	for i in range(gameSize):
		for j in range(gameSize):
			if j>i:#this takes the upper triangle of the matrix
				ownership = conMatrix[i][j]
				if ownership == 0:
					p0.append([i,j])
				if ownership == 1:
					p1.append([i,j])
				if ownership == " ":
					left.append([i,j])
				
	print("RED PLAYER moves so far: ")
	for each in p0:
		print(each)
	
	print(" ")
	print("BLUE PLAYER moves so far: ")
	for each in p1:
		print(each)
	print(" ")
	print("moves remaining: ")
	for each in left:
		print(each)
	print(" ")


def move(player, first, second):
	moved = 0
	if ((first != second) & (first<gameSize) & (first>=0) & (second<gameSize) & (second>=0)):
		if (conMatrix[first][second] == ' '):
			conMatrix[first][second] = player
			moved=1
		if (conMatrix[second][first] == ' '):
			conMatrix[second][first] = player
			moved=1
	else:
		print('invalid move, out of range')
	return moved

def checkLoss(m, c, ai=0):
	
	if m==gameSize:#base case for start of game
		return True
	# check for closed triangles given the most recent move.
	# we do this by DFS of depth 3 on the connectivity matrix
	# move comes in as [a, b]
	# we check DFS on B, and if for example we discover the path
	# A> B> C>A, we have discovered a triange.
	# limit depth to 2, to prevent finding paths of length 4 or more
	
	goal = m[0]
	init = m[1]
	turn = (c-1)%2 #0 or 1
	#DFS is a FIFO stack
	stack = [[0,m[1]]] #[depth, node number]
	visited=[]
	while(len(stack)>0):
		[depth, working] = stack.pop()
		visited.append(working)
		if depth < 2: # closed loops of depth 3 are not triangles.
			for i,player in enumerate(conMatrix[working]):#retrieve the connections of this node
				#print(working,i,"-",depth,"-",player)
				if player == turn:
					if (i == goal) & depth>0: 
						print("*****************************")
						if turn == 0: print("********* RED  LOSS *********")
						if turn == 1: print("********* BLUE LOSS *********")
						print("*****************************")
						return False
					if (i not in visited): stack.append([depth+1, i])
	
	return True

def playGame(pcolor):
	if pcolor == 1: roboColor =0
	if pcolor == 0: roboColor =1
	
	turnColor = 0
	m=gameSize
	while(checkLoss(m, turnColor)):
		print(" ")
		if (turnColor%2 == pcolor):
			print("your turn, please enter your move as 2 numbers")
			m = getPlayerMove()
			while (move(turnColor %2,m[0],m[1])==0):
				print('invalid move, already taken')
				m = getPlayerMove()
		else:
			print("my turn")
			m = getAIMove()
			move(turnColor %2,m[0],m[1])==0
			
			#this line shows the current state of the game
			#showGameState()
		print(" ")
		if turnColor %2 == 0:
			print("---- RED Moves ----")
		else:
			print("---- BLUE Moves ----")
		print(m)
		print("")
		turnColor+=1
	showGameState()
	
	
	
def getPlayerMove():
	m=""
	while (len(m) != 2):
		if (m!=""):
			print("invalid move!, enter 2 numbers")
		i = raw_input("what is your move? Or enter 'game' for game state:  ")
		if i == "game":
			showGameState()
		m = i.strip().split(" ")
	return([int(x) for x in m])


def evalGame(state, moves):
	
	evals = [10 for x in range(len(moves))]
	
	# things that go into evaluating:
	
	# 1 a loss is bad, avoid at all costs (-99)
	# 2 more connections from a single point are bad, try to avoid. (-1 per connection of a node)
	#		having all 7 other points connected to 0 means a loss next turn.
	# 3 a move that takes a potential triangle away from the oponent is bad (-1)
	# 
	
	for mNum,m in enumerate(moves):
		
		#1
		for (i, connection) in enumerate(conMatrix[m[1]]):
			if connection == roboColor:
				for (i2, connection2) in enumerate(conMatrix[i]):
					if connection2 == roboColor:
						if i2 == m[0]:
							evals[mNum] -= 99
		
		#2
		numConnections=0
		for point in m:
			for connection in conMatrix[point]:
				if connection == roboColor:
					numConnections +=1
		evals[mNum] -= numConnections
		
		
		#3
		for (i, connection) in enumerate(conMatrix[m[1]]):
			if connection == playerColor:
				for (i2, connection2) in enumerate(conMatrix[i]):
					if connection2 == (playerColor):
						if i2 == m[0]:
							evals[mNum] -= 1
	
	return evals





def getAIMove():
	#first we get all available moves:
	left = []
	for i in range(gameSize):
		for j in range(gameSize):
			if j>i:	#this takes the upper triangle of the conMatrix
				ownership = conMatrix[i][j]
				if ownership == " ":	#free move
					left.append([i,j])
	
	#we then evaluate each state against the current one.
	evals = evalGame(conMatrix, left)
	
	#find the best move
	bestIndex = evals.index(max(evals))
	
	
	#lastly we return the best option found
	return left[bestIndex]
	
	# note that we could make this process recursive and use A-B pruning. on it. 
	# Check all moves, check all moves from those moves... repeat 3 or so times and bulild a tree of evaluations
	# run minimax on the results of the tree we just found.
	# this isnt needed for this task though, this AI is hard enough to beat as is.
	
	
########################################################
#start of program
print()
print("welcome to sim, current game size is ", gameSize)

print("the points are: ")
print(range(gameSize))


i = raw_input(' do you wish to play as red? (y/n) ')
if (i=='y'):
	playerColor = 0
	roboColor = 1
	print("You go first")
else:
	playerColor = 1
	roboColor = 0
	print("I got first")	
playGame(playerColor)
