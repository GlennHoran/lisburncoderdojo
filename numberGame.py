import random

# making a function
def numberGame():
    # boolean to check if guess is correct
    guessedCorrectly = False
    # finding a random number from 1 - 10
    answer = random.randint(0, 10)
    # Telling user to guess number and setting initial guess
    guess = int((raw_input("Welcome to the number guessing game! Please guess a number between 1 and 10\n")))

    #if user gets guess first time, print congratulations message and set guess boolean to true
    if answer == guess:
        print("Wow you got it first time, incredible!\n")
        guessedCorrectly = True

    #Enters into a loop that asks user to keep guessing until they get it right
    while guessedCorrectly == False:

        #if guess is higher than answer
        if answer < guess:
            guess = int(raw_input("Guess lower!\n"))

        # if guess is lower than answer
        elif answer > guess:
            guess = int(raw_input("Guess Higher!\n"))

        #if guess is correct set guessedCorrectly boolean to true so loop finishes
        elif answer == guess:
            guessedCorrectly = True
            print("You got it! Nice!\n")

#Calling the function so that it will run
numberGame()
