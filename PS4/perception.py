#!/bash/python3

#The perceptron equation is S = sum(wi x xi) from i = 0 to i = n

#The function of the separated line is f(s) = 1 if S >= 0, 0 otherwise. I call it
#a step funciton

from random import choice, randrange, uniform, randint
from numpy import array, dot 

unitStep = lambda x: 0 if x < 0 else 1

trainingData = [ 
        # array([A, B, C, bias]), output)]
        # NOTE: bias is always 1 
        (array([0,0,0,1]), 0), 
        (array([0,1,1,1]), 0), 
        (array([1,0,1,1]), 1), # B doens't matter
        (array([1,1,1,1]), 1), 
        #(array([1,1,0,1]), 1),
        ]

# uniform gives you a floating-point value from -1 to 1
# Initially, choose 3 random values
times = range(4)
ranArr = [uniform(-1, 1) for i in times]
print("ranArr: ", ranArr)

#The errors list is only used to store the error values so that they can be plotted later on
errorData = []
# ETA controls the learning rate
ETA = 0.2
n = 250

#q = random.rand(4)
#print("q: ", q)

for i in range(n):
    x, expected = choice(trainingData)
    #print("X: ",x , "Expected: ", expected)
    #print("dot product", dot(ranArr[i], x))
    #result1 = sum(dot(ranArr[i], x))
    result1 = dot(ranArr, x)
   
    print("result1 is: ", result1)
    
    #we can compare to the expected value. If the expected value is bigger, we need to increase the weights, if it's smaller, we need to decrease them
    error = expected - unitStep(result1)
    errorData.append(error)
    #print("errorData: ", errorData)

    #correction factor is calculated in the last line, where the error is multiplied with the learning rate (eta) and the input vector (x). It is then added to the weights vector, in order to improve the results in the next iteration.
    ranArr[i] += ETA * error * x
    #print("ranArr: " , ranArr)

for x, _ in trainingData:
    result = dot(x, ranArr[i]) 
    #print("ran: ", ranArr[i])
    print("{}: {} -> {}".format(x[:3], result, unitStep(result))) 
   
