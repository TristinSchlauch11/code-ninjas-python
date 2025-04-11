# In this project, we will be coding a Rock-Paper-Scissors game. First, we'll ask the user for their choice, then the computer
# will randomly pick their choice. Then, we'll use if-statements to see if the player won, the computer won, or they tied!


#### DO NOT CHANGE THIS CODE ####
import random
#################################

# Step 1:
# First, let's set up some variables that we will use throughout the game.

# [] Assign a variable called 'ply_input' to be an empty string
# [] Also assign a variable called 'answers' to a list containing the strings 'rock', 'paper', and 'scissors'
# Make sure that these variables have the correct names!



# Step 2:
# Next, we'll ask the player to input one of the three options. Below, there is a while loop that will continue to ask 
# the player to type in an option until they type in one of the options that we defined in our 'answers' list above.

# [] Inside this while loop, ask the player to input 'rock', 'paper', or 'scissors' and store in the 'ply_input' variable
# [] Next, we need to check if the player's input is in our list of answers. If it is not, print a message telling the
# player that their input is not correct

while ply_input not in answers:
    # enter your code here!



# Step 3:
# Now, we need to get the computer's answer. In the code below, the computer will randomly select the number 0, 1, or 2
# and store it in a variable called 'cpu_num'. Notice that there are the same amount of numbers that the computer can pick
# as there are options to pick! You will need to use this random number to get the computer's choice from our 'answers' list.

# [] Use the 'cpu_num' variable to index our list 'answers' to get the computer's choice. This will make the computer pick one
# of 'rock', 'paper', or 'scissors'. Store this pick in a variable called 'cpu_input'
# [] Use a print statement to print the computer's selection to the screen. You can also use string concatentation here!

#### DO NOT CHANGE THIS CODE ####
cpu_num = random.randint(0, 2)
#################################



# Step 4:
# Now, we need to find out if you won against the computer! Remember the rules of rock-paper-scissors:
# 1. Paper covers rock
# 2. Rock smashes scissors
# 3. Scissors cuts paper

# [] Use if-elif-else statements to determine if the player won the game. If the player wins, then
# print "You won!" on the screen. If the computer wins, then print "You lose" on the screen. If there 
# is a tie, then print "Tie" on the screen. A tie happens when both the player and the computer have
# the same answer
# HINT: You need to use either nested if-elif-else loops, or some Boolean connectors (AND, OR, NOT)


