import random
from englishHangman import words

print("Let's play a game of Hangman")
print("============================")
secretWord=random.choice(words).upper()
print("\nI have picked a word that starts with letter "+secretWord[0] + " and ends with "+ secretWord[-1])
updatedGuess=[secretWord[0]] + ["-"]*(len(secretWord)-2) + [secretWord[-1]]
guessesLeft=10
print("\nHere's the template in which each dash denotes a single letter:\n" 
      +" ".join(updatedGuess)
      +"\n\nNow it's your turn to guess a letter. You have " + str(guessesLeft) + " guesses left")


while guessesLeft>0:
    
    guess=input("Please enter your next guess: ").upper()
    
    if guess in secretWord: #test if guess is correct
        #guess is CORRECT
        print("Correct")
        
        for i in range(len(secretWord)):
            if guess==secretWord[i]:
                updatedGuess[i]=guess
        
        
        
        print(" ".join(updatedGuess))
        
        if "".join(updatedGuess)==secretWord:
            print("\nYou won,congrats!")
            break
                

    else:
        #guess in INCORRECT
        print("\nIncorrect. Letter " + guess + " does not occur in this word.")
        guessesLeft-=1
        print("You have "+str(guessesLeft)+" guesses left")
        
if guessesLeft==0:
    print("\nYou lost this game. The word is "+secretWord)
    
