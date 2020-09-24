import random
import time

#Intro
playerName = str(input("What is your name?\n"))
print("Hello, %s!" % playerName)

def main():
    startGame = str(input(f"Tell me, {playerName}, do you want to play some Hangman?\n")).upper()
    if startGame == "YES":
        print("Let's start!")
    else:
        print("Are you sure you don't want to play?")
        time.sleep(2)
        print("That's a shame")
        exit()

    #Setting tries 
    tries = 0
    maxTries = 6
    endGame = False

    #Generating word
    randomWord = (random.choice(open("words_alpha.txt").read().upper().split()))
    hidden = []
    for character in randomWord:
        hidden.append("_")


    print("You have 6 tries to guess the letters in the word, or else you lose!")
    time.sleep(2)

    while endGame == False:
        print(f"The word is: {' '.join(hidden)}")
        letterGuess = str(input("Please guess one of the letters.\n")).upper()
        if len(letterGuess) == 1 and letterGuess in randomWord:
            for i in range(0, len(randomWord)): # for i in range of 0 to the length of the word 
                letter = randomWord[i] # letter is one of the letters in the random word 
                if letterGuess == letter: # if letter guess is equal to one of the letters in the random word
                    hidden[i] = letterGuess
        if "_" not in hidden:
            break

        if letterGuess not in randomWord:
            print(f"Oh no, '{letterGuess}' is not in the word!")
            time.sleep(1)
            tries += 1
            triesLeft = maxTries - tries 
            print(f"You have {triesLeft} tries left.")
            
            if tries >= maxTries:
                print("You have lost! You have failed to guess the letter to many times!")
                time.sleep(1)
                print(f"The word was, {randomWord}.")
                time.sleep(1)
                restart = str(input("Do you want to try again?\n")).upper()

                if restart == "YES":
                    print("Great!")
                    time.sleep(1)
                    main()
                else:
                    print("That's a shame")
                    time.sleep(1)
                    exit()

   
    print(f"CONGRATULATIONS, {playerName}! You have won a game of hangman!")
    time.sleep(2)
    reset = str(input("Do you want to play again?\n")).upper()
    if reset == "YES":
        print("Yay!")
        time.sleep(2)
        main()
    else:
        print("Are you sure?")
        print("Okay then")
        exit()

   

         














main()
    
    

























































