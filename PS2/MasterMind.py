#!usr/bin/env python

import random

colors = ["R", "B", "O", "W"]
trials = 0
getSolution = True
nothingRight = False

print ("Welcome to mastermind \n")
print ("red(R), blue(B), orange(O), white(W)")

#random choose 3 colors from array colors and store to secretCode
secretCode = random.sample(set(colors), 3)
print (secretCode)

def outputNothingRight():
    print ("Your answer: nothing(no X's or O's)")

# user play the game until finish it or 8 times
while getSolution:
    rightColor = ""
    #rightColor = []
    guessColor = ""
    #guessColor = []
    playerGuess = raw_input("Enter the color code: ").upper()
    trials = trials + 1
    #print (playerGuess), trials

    #check if the input from the user is right or not
    if len(playerGuess) != len(secretCode):
        print ("The amount of code should be 3. Try again")
        continue
    
    for i in range(3):
        if playerGuess[i] not in colors:
            print ("The color code you entered is not valid")
            continue

    # here is trying to compare the user input and secret code
    if rightColor != "XXX":
        for j in range(3):
                # X is right position and right color
            if playerGuess[j] == secretCode[j]:
                #rightColor.append("X")
                rightColor = rightColor + "X"
            
                #right color but wrong position
            elif playerGuess[j] != secretCode[j] and playerGuess[j] not in secretCode:
                #guessColor.append("O")
                #guessColor = guessColor + " "
                nothingRight = True
                if(nothingRight):
                    outputNothingRight()
                    nothingRight = False
                    break;
            elif playerGuess[j] != secretCode[j]:
                if playerGuess[j] in secretCode:
                    guessColor = guessColor + "O"
            elif playerGuess[j] != secretCode[j]:
                if playerGuess[j] not in secretCode:
                    guessColor = guessColor + " "

        print ("Your answer: ") + rightColor + guessColor + "\n"
    
    # here is to see how many time the user guesses to win
    # 'X' is right position and right color
    if rightColor == "XXX":
    #for i in rightColor:
    #    if rightColor[i] == secretCode[i]:
        if trials == 1:
            print ("Did you cheat to win at the first try?")
        else:
            print ("Good job! You used " + str(trials) + " trials.")

        getSolution = False

    # display the user next movement or game over
    if rightColor != "XXX" and trials < 8 and trials >= 1:
        print ("Next trial: ")
    elif trials >= 8:
        print ("You lose. The secret code was: " + str(secretCode))
        getSolution = False

    while getSolution == False:
        ansToPlay = raw_input("Want to play again?(y/n) \n").lower()
        trials = 0
        if ansToPlay == 'y':
            getSolution = True
            print ("New round has started: \n")
            print ("What's the secret code: \n")
        else:
            print ("Peace out")
            break
