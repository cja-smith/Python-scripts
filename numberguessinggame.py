from random import randint

def user_guess():
    global NumberOfGuesses

    while True:
        print(f"You have {10-NumberOfGuesses} guesses left.")
        guess = input()
        
        try:
            guess = int(guess)
            
            if guess in range(101):
                NumberOfGuesses+=1
                return guess
            
            else:
                print("That's not within the range!")
        
        except ValueError:
            print("Try an integer!")
            
def checkandclues(guess,n):
    #Gives clues based on higher/lower, range, factors, and multiples
    if guess == n:
        print("You got it!")
        return True
    
    elif guess in range(n-5,n+6,1):
        print("Close!\nClue: You're within 5 of the number I'm thinking of!")
        return False
    elif guess > n:
        print("Too high!")
        if guess%n==0:
            print("Clue: That guess is a multiple of the number I'm thinking of.")
        else:
            pass
        return False
    elif guess < n:
        print("Too low!")
        if n%guess==0:
            print("Clue: That guess is a factor of the number I'm thinking of.")
        else:
            pass
        return False


#game logic goes here
while True:
    print("Hello! I am thinking of a number between 1 and 100, and you have 10 guesses to try and work out which number it is.\nGood Luck!")
    n=randint(0,100)
    play_game = input("Ready to begin? Type y or n")
    
    if play_game.lower() == "y":
        NumberOfGuesses=0
    else:
        break 
    
    while NumberOfGuesses<10:
        
        if checkandclues(user_guess(),n):
            NumberOfGuesses = 110 #break out of the while loop
            break
        
        #takes user input
        #check and give clues
        checkandclues(user_guess(),n)

            
    if NumberOfGuesses==110:
        print("Congratulations!")
        replay = input("Would you like to play again? Type y or n")
    
        if replay.lower() == "y":
            continue
        else:
            break
    else: 
        print(f"Sorry you used too many guesses! The number I was thinking of was {n}!")
        replay = input("Would you like to play again? Type y or n")
    
        if replay.lower() == "y":
            continue
        else:
            break

            