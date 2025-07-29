# In this project, you will creating the classic Hangman game! The player will attempt to guess a secret word one
# letter at a time until either they guess all the letters in the secret word, or they run out of lives!

# Step 1:
# First, we need to define some variables that we are going to use throughout the program
# [O] Define a variable called 'word_to_guess' that contains your secret word! Please make your word all lowercase!
# [O] Next, define an empty list called 'guesses' that will hold all of the guesses the player has made so far.
# [O] Finally, define a number called 'lives' and set it equal to 7. This is the number of wrong guesses that the
# player is allowed to make.

word_to_guess = "mountain"
guesses = []
lives = 7

# In the code below, we convert your secret word to a list of letters and store this list in the variable 'answer'.
# For example, 'code' would be converted to ['c', 'o', 'd', 'e']
# ['j', 'u', 'n', 'g', 'l', 'e']
#### DO NOT CHANGE THIS CODE ####
answer = list(word_to_guess)
#################################


# Step 2:
# We're going to define two functions for this program. First, we'll define a function that prints the word with
# letters that the player has guessed so far. For letters that the player has not guessed yet, we'll print an
# underscore ("_") instead.

# [O] Start off with defining this function as "print_word_so_far". It needs no parameters.
# [O] Assign a variable 'message' to an empty string. You will update this string with string concatenation
# throughout the function
# [] Now, we need to iterate through every letter in our 'answer' list. If the letter has been guessed, we will
# update our 'message' by concatenating it with both the letter and a space.
# HINT: The list 'guesses' contains all the letters that have been guessed by the player so far. How can we use
# this list to check if the letter in our answer has been guessed or not
# [] If the letter has NOT been guessed by the player, then we will update our message by concatenating it with
# the string "_ ". Remember the space!
# [] Finally, after the for loop has finished, print the 'message' variable on the screen.

def print_word_so_far():
    message = ""
    for letter in answer:
        if letter in guesses:
            message = message + letter + " "
        else:
            message = message + "_ "
    print(message)
        
# Step 3:
# Our other function is going to be a Boolean function that we will use as a condition in a while loop. This
# function will check if the player has correctly guessed the word by checking if each letter in the answer
# has been guessed.

# [O] Start off by defining this function with the name "guessed". It doesn't need any parameters.
# [] Now, we need a for loop to iterate over each letter in our 'answer' list and check if it has been guessed 
# by the player. If any letter has not been guessed, we know that the word has not been guessed yet! We should 
# immediately end the function and return False.
# [] If we check all the letters and can't find any that have not been guessed, the player has correctly guessed 
# the word! To say this, we can write the code "return True" outside the for loop.

def guessed():
    for letter in answer:
        if letter not in guesses:
            return False
    return True

# Step 4:
# Now, we'll write the code for the Hangman game. Since we need to ask the player for an unknown number of
# letters, we need to use a while loop. We will continue to ask the player for letters until they run out of
# lives or they guess the word.

# [] Write the first line of the while loop. This loop should continue to run until the player runs out of lives
# or until the word is guessed. Remember, to check if the word has been guessed, you can call the guessed()
# function that you defined in Step 3.
# [] Inside the loop, call the print_word_so_far function, and print the number of lives that the player has left
# [] Next, ask the player for a lowercase letter, and store this input in a variable called 'letter'

while lives > 0 and not guessed():
    print_word_so_far()
    print("Lives Left: " + str(lives))
    letter = input("Please enter a lowercase letter ")

    #### DO NOT CHANGE THIS CODE ####
    if not letter.isalpha() or not letter.islower() or len(letter) != 1:
        print("Not a valid letter!")
        continue
    #################################

    # Step 5:
    # Now, we need to check the letter that the player entered.
    
    # [] Use an if statement to check if the player has guessed that letter already. If they have, print a message
    # telling the player that they have guessed the letter already
    # [] If they haven't guessed the letter already, we need to add it to their list of guesses. Then, we need to
    # check if their guess is in the word
    #   [] If the guess is in the word, print a message saying that the player has guessed a letter!
    #   [] If the guess isn't in the word, print a message saying that the player has lost a life, and decrease
    #   their life count by 1.

    if letter in guesses:
        print("You have already guessed that letter!")
    else:
        guesses.append(letter)
        if letter in word_to_guess:
            print("You guessed a letter!")
        else:
            print("Not in the word! You lose a life")
            lives = lives - 1

# Step 6:
# Now, we need to code the end of the Hangman game. If the player guesses the word before they run out of lives,
# they win! However, if they run out of lives, they lose.

# [] Use an if-statement to determine if the player has won or not. If the player has won, print a winning message!
# [] If the player lost, print a losing message and the correct word on the screen for the player to read.

if lives == 0:
    print("You lose!")
else:
    print("You won!")
