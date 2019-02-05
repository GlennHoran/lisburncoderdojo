import random


def numberGame():
    guessedCorrectly = False
    answer = random.randint(0, 10)
    print(answer)
    guess = int((raw_input("Welcome to the number guessing game! Please guess a number between 1 and 10\n")))
    if answer == guess:
        print("Wow you got it first time, incredible!\n")
        guessedCorrectly = True

    while guessedCorrectly == False:
        if answer < guess:
            guess = int(raw_input("Guess lower!\n"))
        elif answer > guess:
            guess = int(raw_input("Guess Higher!\n"))
        elif answer == guess:
            guessedCorrectly = True
            print("You got it! Nice!\n")



response = 0
name = raw_input("Hello, what is your name? \n")
print("Hello " + name + "I am a VERY basic chat bot. Just like Amazon's Alexa, except I am not that smart =(")
while response != "4":
    response = raw_input("""What would you like to do?
  1. What's the weather today?
  2. let's play a number guessing game 
  3. let's play hangman
  4. quit\n""")

    if response == "1":
        print("\n Well it's Lisburn, so it's probably raining\n")
    elif response == "2":
        numberGame()
    elif response == "3":
        print("\nI can't play hangman yet...\n")
    elif response == "4":
        print("\ngoodbye!\n")











