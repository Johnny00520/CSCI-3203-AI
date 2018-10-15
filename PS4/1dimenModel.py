#!/bash/python3

#each element of neighbotModel is a house, we begin with all random int from 0 to 2 without 
# beyond 6 for 0. 27 for 1, 27 for 2.
#I generat a value(num), which is an index of list, neighborModel and compare its neighbots
#, if it has two same kind of types, it will print "The number is satisfied", not otherwise.
# If the random number in the list is satisfied, the list doesn't swap. If it's not, then swap.

# Choose a random index for the list and output 6 more indexes from the chosen index

from random import randint
from collections import Counter
neighborModel = []

def generateRanArr():
    keepGenerating = False
    numCounter = 3
    zeroCounter = 1 # < 6
    oneCounter = 1 # < 27
    twoCounter = 1 # < 27

    while(not keepGenerating):
        m = randint(0, 2)

        # Make the first 3 elements different
        if m not in neighborModel:
            neighborModel.append(m)
        else:
            if m == 0 and zeroCounter < 6:
                neighborModel.append(m)
                zeroCounter = zeroCounter + 1

            elif m == 1 and oneCounter < 27:
                neighborModel.append(m)
                oneCounter = oneCounter + 1

            elif m == 2 and twoCounter < 27:
                neighborModel.append(m)
                twoCounter = twoCounter + 1

        if(zeroCounter + oneCounter + twoCounter == 60):
            keepGenerating = True

#Check a random dissatisfied occupant
def checkSatisfied(num, indexZero, numZero):

    #print("num is: ", num)
    #print("numZero: ", numZero)
    #print("Old indexZero: ", indexZero)
    
    if(num == 58):
        if (neighborModel[num + 1] == neighborModel[num] and neighborModel[0] == neighborModel[num]):
            print("The number is satisfied")
    elif(num == 59):
        if (neighborModel[0] == neighborModel[num] and neighborModel[1] == neighborModel[num]):
            print("The number is satisfied")
    # Check if the random occupant is happy
    elif (neighborModel[num + 1] == neighborModel[num] and neighborModel[num + 2] == neighborModel[num]):
        print("The number is satisfied")
    elif (neighborModel[num - 1] == neighborModel[num] and neighborModel[num -2] == neighborModel[num]):
        print("The number is satisfied")
    else:
        print("The number is NOT satisfied")
        #print("trackIndexZeroList: ", indexZero[numZero])
        swap = neighborModel[num]
        neighborModel[num] = neighborModel[indexZero[numZero]] 
        neighborModel[indexZero[numZero]] = swap
    
    indexZero = [i for i, index in enumerate(neighborModel) if index == 0]
    #print("new indexZero: ", indexZero)
    #print ("new neighborModel: ", neighborModel)

generateRanArr() 
counter = 1
i = 1

for i in range(400):
    first = []
    last = []
    #print(Counter(neighborModel))
    #print("Old neighborModel: ", neighborModel)
    
    # find indexes of 0 (empty occupant) in list
    indexZero = [i for i, index in enumerate(neighborModel) if index == 0]
    
    # Pick a value from 1 to 60
    num = randint(0, 59)
    # Pick a random value for indexZero
    numZero = randint(0, 5)

    checkSatisfied(num, indexZero, numZero)
    counter = counter + 1
    # Output from a random index of list to 5 values more
    if(counter % 20 == 0):
        ranSixDigitIndex = randint(0, 59)
        print("ranSixDigit: ", ranSixDigitIndex)
        
        # Handle some certain cases, and extend the output array
        if(ranSixDigitIndex == 55):
            first = neighborModel[:1]
            last = neighborModel[-5 : ]
            last.extend(first)
            print(last)
            #print(neighborModel[-5: 0])
        elif(ranSixDigitIndex == 56):
            first = neighborModel[:2]
            last = neighborModel[-4 : ]
            last.extend(first)
            print(last)

            #print(neighborModel[-4: 1])
        elif(ranSixDigitIndex == 57):
            first = neighborModel[:3]
            last = neighborModel[-3 : ]
            last.extend(first)
            print(last)

            #print(neighborModel[-3 : 2])
        elif(ranSixDigitIndex == 58):
            first = neighborModel[:4]
            last = neighborModel[-2 : ]
            last.extend(first)
            print(last)

            #print(neighborModel[-2 : 3])
        elif(ranSixDigitIndex == 59):
            first = neighborModel[ : 5]
            last = neighborModel[-1: ]
            last.extend(first)
            print(last)
            #print(neighborModel[-1 : 4])
        else:
            print("six digits neighborModel", neighborModel[ranSixDigitIndex: ranSixDigitIndex + 6])

        print(counter)


print ("new neighborModel: ", neighborModel)
