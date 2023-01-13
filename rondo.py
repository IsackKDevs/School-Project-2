#Random Number Guessing Game
#Isack Kipanga
#10/07/2022

#tthe "main" function calls the other functions
def main():
    generateNumber() 
    inputUserGuess()
    displayAnswer(generateNumber, inputUserGuess)

#below we have the code that will generate a random number
#using the random.randint to generate a random number
#returning the randomNumer variable
#the import random, imports the random libray
def generateNumber():
    import random
    randomNumber = random.randint(1, 100)
    return int(randomNumber)

#below is the code for getting a number input from the user, any random number
#then return the number gotten from the user's input
#i'm using int(input("")) in order to get a number input
def inputUserGuess():
    guessNumber = int(input("I am thinking of a number. What is the number? "))
    return guessNumber

#to display the answer input of both  the user and the randomized number
#we get both of the numbers and check them if they are matched, using the if, else statement we are able to judge if two numbers are equaled
#if the user's input number matches the random number generated then it will print "you have guessed correctly" otherwise
#it will display "Sorry, your guess is incorrect. I was thinking of " the generated number 
def displayAnswer(randomNumber, guessNumber):
    if randomNumber == guessNumber:
        print("You guessed correctly!")
    else:
        print("Sorry, your guess is incorrect. I was thinking of " + str(randomNumber()))

#this calls all the functions    
main()
