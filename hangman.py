import hint
import random
import display_hangman
import anim


fruits = [
    "apple", "banana", "cherry", "peach", "watermelon"
    "grapes", "mango", "orange", "pineapple", "strawberry"
]
cities = [
    "Mumbai", "Delhi", "Jaipur", "Varanasi", "Agra", 
    "Mysore", "Shimla", "Amritsar", "Goa", "Ooty"
]


def hangman():
    print("Welcome to the game!!!")
    inp = set()
    guess = random.choice(fruits)
    chances = 6
    while chances > 0 :
        display_hangman.display_pic(chances)
        print(f"Hint: {hint.hint(guess)}")
        print("Word : ",hint.disp_word(guess, inp))
        print("Remaining chances : ", chances)
        print(f"Guessed Letters : {' '.join(sorted(inp)) if inp else 'None'}")
        
        user_guess = input('Enter the next guess : ').lower() #Makes all user_guesses in lower.
        
        if len(user_guess) != 1 or not user_guess.isalpha() : #Checks for valid inputs.
            print("The guess was not appropriate. Please enter a single letter as your user_guess.")
            continue

        if user_guess in inp : #Checks whether the letter has already been user_guessed.
            print("You have already user_guessed this letter please try again")
            continue

        inp.add(user_guess) #Adds the letter to the set of user_guessed letters.

        if user_guess in guess:
            print("Good job! You guessed a letter correctly.")
            if set(guess) <= set(inp):
                print("Congratulations! You've guessed the word:", guess)
                anim.draw_stickman()
                break

        else:
            print("Oops! That letter is not in the word. Try Again")
            chances-=1

    if chances == 0 :
        print("Gameover. You have lost the game. The word was", guess, ". Better luck next time.")

    
    
