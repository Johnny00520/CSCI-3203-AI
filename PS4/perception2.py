#!/bash/python

#The perceptron equation is S = sum(wi x xi) from i = 0 to i = n

#The function of the separated line is f(s) = 1 if S >= 0, 0 otherwise. I call it
#a step funciton

from random import choice 
from numpy import array, dot, random

unitStep = lambda x: 0 if x < 0 else 1 

training_data = [ 
        # array([A, B, C, bias]), expected output)]
        # NOTE: bias is always 1 
        (array([0,0,0]), 0), 
        (array([0,1,1]), 1), 
        (array([1,0,1]), 1), 
        (array([1,1,1]), 1), 
        ] 

# uniform gives you a floating-point value from -1 to 1
# Initially, choose 3 random values for weight
w = [random.uniform(-1, 1) for i in range(3)]
print("Random weights are: ", w)

#The errors list is only used to store the error values so that they can be plotted later on
errors = [] 

# ETA controls the learning rate
ETA = 0.2 
n = 8001 

for i in xrange(n): 
    x, expected = choice(training_data) 
    result = dot(w, x) 

    #we can compare to the expected value. If the expected value is bigger, we need to increase the weights, if it's smaller, we need to decrease them
    error = expected - unitStep(result) 
    errors.append(error) 
    w += ETA * error * x 
    
    #print("w: ", w)
    if i % 250 == 0:
        print(i)
        print("weight is: ", w)
        print("unitStep: ", unitStep(result))
        #print("error array: ", errors)
    
for x, _ in training_data: 
    #print("x: ", x)
    #print("_: ", _)
    #print("w: ", w)
    result = dot(x, w) 
    print("{}: {} -> {}".format(x[:3], result, unitStep(result)))

