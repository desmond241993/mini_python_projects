#lets create a new game - GUESS THE NUMBER

import random
import time 

print("\t>>>>> GUESS THE NUMBER <<<<<\n")

#method to check if the user guess is correct
def checkUserInput(actual,guess):
    print("Comparing user input with generated number...")
    time.sleep(2)
    if actual == guess:
        return True
    else:
        return abs(actual - guess)
 
#method to generate a random number that the user need to guess       
def generateNumber():
    print("Generating number...please wait\n")
    n = random.randint(0,9) #generate a number between 0 and 9
    time.sleep(2)           # wait for 3 sec
    print("Number generated successfully\n")
    return n 
 
score = 0       #score for correct guess
no_of_guess = None 

no_of_guess = int(input("How many guesses would you like to make: "))
g = no_of_guess       #temporarily store the number of guesses

#loop through until the guesses run out
while(no_of_guess > 0):
    guess = None
    
    #promt user to re-enter until the input is a number 
    while guess is None:
        try:
            guess = int(input("Take your guess: "))
        except ValueError:
            print("Not a number...try again")
    
    #generate a random number
    num = generateNumber()
    
    #check user guessed number 
    check = checkUserInput(num,guess)
    if(check == True):
        print("Successful guess...you are really good in this")
        score += 1 
        print("You have scored a point")
    else:
        print("You missed by a margin of "+str(check))
        print("Bettter luck next time...\n")
    no_of_guess -= 1

print("\n\tFINAL RESULT\n")
if score == 0:
    print("You failed to score anything")
else:
    print("You have scored "+str(score)+" out of "+str(g)+" guesses")
