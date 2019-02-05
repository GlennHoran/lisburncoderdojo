from numberGame import numberGame
response = ""
name = raw_input("Hello, what is your name? \n")
print("Hello " + name + "I am a VERY basic chat bot. Just like Amazon's Alexa, except I am not that smart =(")

while response != "9":
    response = raw_input("""What would you like to do?
  1. What's the weather today?
  2. let's play a number guessing game 
  9. quit\n""")

    if response == "1":
        print("\n Well it's Lisburn, so it's probably raining\n")
    elif response == "2":
        numberGame()
    elif response == "9":
        print("\ngoodbye!\n")











