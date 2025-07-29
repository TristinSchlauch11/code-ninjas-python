# In this project, you will code a number guessing game! The computer will randomly select a number between 1 and 100,
# then the player will try to guess it. With each guess, the computer will tell you if the actual number is higher or
# lower. You can also ask to see a list of all your guesses so far and if they were too high or too low. When the
# player guesses the number, the computer will also print the amount of guesses that it took for them to guess it.

###### DO NOT CHANGE THIS CODE ######
import random
num_to_guess = random.randint(1, 100)
#####################################

# Step 1:
# [] Before anything else, we're going to define an empty list called 'guesses' that will store the guesses that our
# player makes throughout the game.



# Step 2:
# Now, we're going to create a function that will allow us to print all of the guesses that we've made so far. With
# each guess, we'll also say if the guess was too high or too low.

# [] Define a function called 'print_guesses'. This function does not need any parameters.
# [] Use an if statement to check if the player has made no guesses. If they have not made any guesses, then print a 
# message telling them that they haven't made any guesses, then immediately exit the function by using 'return'
# HINT: The list 'guesses' stores all of the guesses that the player makes. What can we say about this list if no 
# guesses have been made?
# [] Next, we'll need to iterate over all guesses in this list. For each guess in the list, if the guess was too high,
# print the number that was guessed onto the screen and a message saying that it was too high. If the guess was too
# low, print the number and that it was too low. 
# HINT: You might need to convert the integer to a string if you use string concatenation in your messages.



# Step 3:
# [] Print a welcome message to the player, and explain the rules of the game.



# Step 4:
# Since we need to ask the player for an unknown amount of numbers, we need to use a while loop. Until the player has
# guessed the number, we need to keep asking the player for a number between 1-100. As well, if they enter the number
# 0, we will display all of the guesses that the player has made so far.

# [] Write the first line of the while loop. This while loop will continue until the player has correctly guessed the
# number 'num_to_guess', which is already defined at the top of the program.
# HINT: The list 'guesses' stores all of the guesses that the player makes. What can we say about this list if the
# player hasn't guessed 'num_to_guess' yet?
# [] Inside the while loop, ask the player for their next guess between 1-100, or to enter 0 to see all of their
# guesses so far. Store this number in a variable called 'next_guess'. Remember to convert this input from a 
# string into an integer!!
# [] Now, we need to check the number that the player entered. If the player entered the number 0, then we can call the
# 'print_guesses' function that we already defined and it will print all of the player's guesses!
# [] If the number is either less than 0 or greater than 100, the player has picked an invalid number! Print a message
# telling the player that they have picked an invalid number.



# Step 5:
# Now that we have confirmed that the player has guessed a number between 1 and 100, we need to check if the guess is
# correct, too high, or too low. In the while loop that you started in Step 4, you will complete the 'else' case with the
# following code.

# [] Add the player's guess to the list of guesses that they've made so far.
# [] Now we need to check if the player has guesed the number or not! If the player's guess is equal to the number they 
# need to guess, print a "You win!" message. As well, print the number of guesses that it took for the player to guess the
# number. Remember to convert the integer for the number of guesses to a string if you're using string concatenation.
# [] If the player's guess was bigger than the number to guess, print "Too high".
# [] If the player's guess was smaller than the number to guess, print "Too low".

# REMEMBER!! ALL OF THE CODE FOR STEP 5 SHOULD BE IN THE ELSE CLAUSE IN STEP 4!