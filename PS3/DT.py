import random
import math

accuracy = 4
TreeSplits = []
devMode = False #prints out extra info if dev mode toggle is on

#I chose to do a decision tree for selecting the last class to put in my schedule.

# 25 datapoint examples are in format of:
#  [name, sched conflict, interest level, FCQ course, FCQ teacher, FCQ hrs/week, friends in class, yes/no]

#note: this is not actually real data about my registration for this semester. I just took the highest responded to FCQs and put in some other dummy data.

trainingData = [ [1300, 0, 3, 3.9, 3.5, 12, 0, 0],
                 [1320, 0, 2, 3.6, 3.5, 12, 0, 0],
                 [2270, 1, 5, 4.9, 5.2, 10, 0, 1],
                 [2400, 1, 1, 4.2, 4.5, 12, 0, 0],
                 [2824, 0, 5, 5.2, 5.5, 7,  1, 1],

                 [3002, 1, 1, 3.9, 4.7, 4,  1, 0],
                 [3104, 0, 5, 4.4, 4.7, 15, 0, 1],
                 [3753, 0, 2, 4.1, 4.0, 7,  1, 0],
                 [4318, 1, 4, 5.0, 5.3, 15, 1, 0],
                 [4448, 0, 3, 4.1, 4.4, 9,  0, 1],

                 [4502, 0, 4, 4.0, 4.1, 4,  1, 1],
                 [4831, 1, 5, 5.1, 5.6, 8,  1, 0],
                 [4832, 0, 5, 5.3, 5.6, 7,  0, 1],
                 [5622, 1, 5, 5.4, 5.0, 12, 1, 0],
                 [5832, 1, 4, 3.8, 3.8, 7,  0, 0],

                 [6420, 0, 5, 4.2, 4.4, 8,  1, 1],
                 [1240, 1, 2, 4.8, 5.3, 6,  0, 0],
                 [4229, 0, 5, 4.8, 5.5, 15, 0, 1],
                 [1200, 1, 4, 4.6, 4.7, 7,  0, 0],
                 [3656, 1, 3, 5.1, 5.3, 9,  1, 0],

                 [7000, 1, 2, 6.0, 6.0, 7,  1, 0],
                 [4239, 1, 3, 5.1, 5.7, 12, 0, 0],
                 [3155, 1, 1, 3.0, 5.0, 15, 1, 1],
                 #ran out of FCQ points from last year, had to make up some classes
                 [1111, 1, 5, 4.9, 5.2, 10, 0, 0],
                 [7777, 1, 2, 5.2, 5.5, 7,  0, 0]
                 ]



#step 1: select 5 to use as testers
testData = []
testData.append(trainingData.pop(random.randint(0,len(trainingData)-1)))
testData.append(trainingData.pop(random.randint(0,len(trainingData)-1)))
testData.append(trainingData.pop(random.randint(0,len(trainingData)-1)))
testData.append(trainingData.pop(random.randint(0,len(trainingData)-1)))
testData.append(trainingData.pop(random.randint(0,len(trainingData)-1)))


if devMode:#prints out extra info if dev mode toggle is on
    print("TestData:")
    for i in testData:
        print(i[0])

    print("starting program:")



def entropy(data):
    n = len(data)
    yes = 0
    for each in data:
        if each[7] == 1:
            yes += 1
    no = n-yes

    e=0
    if yes > 0: #this is in here so you cant take the log(0) as that returns -inf or error
       e += -1*(yes/n) * math.log(float(yes)/n,2)
    if no > 0:
        e += -1*(no/n) * math.log(float(no)/n,2)

    return e



def infoGain(datapoints, index, value):
    (groupA, groupB) = split(datapoints, index,value)

    n = len(datapoints)
    a = len(groupA)
    b = len(groupB)

    info = (a/n)*entropy(groupA)+(b/n)*entropy(groupB)
    return entropy(datapoints) - info



def split(data, index, value):
    a=[]
    b=[]

    for point in data:
        if point[index] > value:
            a.append(point[:])
        else:
            b.append(point[:])
    return (a, b)



def makeSubTree(datapoints):

    if entropy(datapoints)==0:
        return False

    maxInfoGain = 0
    bestSplit = (0,0)

    for ind in range(1,7):
        Min=999999999999999
        Max = -9999999999999
        for each in datapoints:
            if each[ind] <Min:
                Min = each[ind]
                #print("Min: ", Min)
            if each[ind] >Max:
                Max = each[ind]
                #print("Max: ", Max)


        if devMode:#prints out extra info if dev mode toggle is on
            print("devMove")
            print(ind, Min, Max)


        step = ((Max-Min)/accuracy)
        for val in [(Min+(step*i)) for i in range(0, accuracy)]:
            i = infoGain(datapoints, ind, val)
            if i > maxInfoGain:
                maxInfoGain = i
                bestSplit = (ind, val)
    if bestSplit == (0,0):
        return False

    print("Best Split: ")
    print(bestSplit, maxInfoGain)
    (i, v) = bestSplit
    TreeSplits.append([i,v])
    a, b = split(datapoints, i,v)
    #print("aaa: ", a)
    print("a:    " + str(len(a)))
    madeA = makeSubTree(a)
    print("b:    "+str(len(b)))
    madeB = makeSubTree(b)

    if not madeA:
        for each in a:
            print(each[0], each[7])
        print()
    if not madeB:
        for each in b:
            print(each[0], each[7])
        print()



    return True
TreeSplits = []
#devMode = True
makeSubTree(trainingData)


print("")
print("")
print("")
print("")

print("splits")
print("=========")
for split in TreeSplits:
    print(split)
print()


print("TestData:")
print("=========")
for i in testData:
    print(i[0])
