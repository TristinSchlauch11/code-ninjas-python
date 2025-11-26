# Welcome to our first project! In this project, we will be (sort of) coding the game Yahtzee!
# Yahtzee is a dice-rolling game where the player attempts to roll certain combinations of dice
# to score points. The player has 5 dice to roll and 3 turns to roll these dice to get the
# combinations they want. Between turns, they can choose to "keep" any dice they choose and roll
# the other ones to increase their chances of rolling one of the scoring combinations.
# Your job will be to code the dice rolling and keeping sections of the game. You do not have to
# code checking if you rolled specific combinations or scoring, that has already been done for
# you. Have fun!

# Step 1
# First, since rolling the dice is a random event, we need to import the random module.
# We'll also set up some variables that the rest of our program will use.
# [O] Import the random module
# [O] Assign a rolls_left variable to the number 3
# [O] Assign a kept_nums variable to an empty list
import random
rolls_left = 3
kept_nums = []

# Step 2
# Next, you're going to define a function called roll that will roll the dice and return a list of
# the numbers that were rolled. This function will take 1 parameter: dice_to_roll, which is the
# number of dice that need to be rolled.
# [O] Start by defining the dice function and giving it the dice_to_roll parameter
# [O] Next, define a variable called rolls to be an empty list
# [] Next, use a for loop to generate a random number between 1 and 6 for all the dice you need to roll
#    Append each of these numbers to the rolls list
# HINT: You will need to use a range function in the for loop
# [] Finally, after all the rolls are done, return the rolls list
def roll(dice_to_roll):
    rolls = []
    


# Step 3
# Here, you have a partially started function called pick_dice. It has 1 parameter called nums which
# is a list of all 5 dice that have been rolled. In this function, the player will get to pick which
# of the 5 dice they want to keep and returns a list of these numbers. You need to finish the function.
# Please do not change any of the code that is already here.
def pick_dice(nums):
    done = False
    keep = []       # the list where you will store the numbers the player wants to keep

    while not done:
        # In this code, we print all of the numbers that the player rolled
        # DO NOT CHANGE THIS CODE
        print("You rolled these numbers:")
        print(nums)
        print("Please pick which ones you want to keep.")

        # [] Here, you need to make a for loop that goes over each number in the nums list and ask the
        #    player if they want to keep it. 
        #    [] Use an input statement to print each number to the screen
        #    [] Use a string comparison to decide if the player wants to keep it or not
        #    [] If they do want to keep it, append it to the 'keep' list
        
        # In this code, we print all the numbers the player rolled, and the numbers they want to keep
        # DO NOT CHANGE THIS CODE
        print("You rolled these numbers:")
        print(nums)
        print("You want to keep these numbers:")
        print(keep)

        # [] Here, you need to confirm with the player if these are the numbers they want to keep
        #    [] Use an input statement and a string comparison to confirm with the player
        #    [] If the player confirms that they want these numbers, return the keep list
        #    [] Otherwise, set the keep list to a blank list and allow the player to pick again 


# Step 4
# We now have all the functions that we need to play the game! Let's create a while loop to play it!

# [] Create a while loop that runs while the player has at least 1 roll left and have kept less than 5 dice
#    That is, if the player keeps all 5 dice, the loop will end
# [] During each turn, you need to do the following:
#    [] Call the roll function to roll the number of dice we need. Store it in a variable called 'rolled_nums'
#    [] Create a new list called 'all_nums' by combining 'kept_nums' and 'rolled_nums'
#    [] Decrease our number of rolls left by 1
#    [] Decide which dice from 'all_nums' to keep by calling pick_dice and storing the result in 'kept_nums'
#        [] But, if the player has no more turns left, they MUST keep all the numbers that they have



# If you want, you can check the code below to see how we check if a scoring combination was rolled
### DO NOT CHANGE THIS CODE ###
print("On your final roll, you rolled these numbers:")
print(kept_nums)

def of_a_kind(rolls):
    '''
    Checks if the player rolled a 3-of-a-kind, 4-of-a-kind, or a Yahtzee
    Also checks for a full house
    '''
    # sort numbers
    # if there is any 3, 4, or 5 of a kind, the number with index 2 must be in it
    sorted_rolls = sorted(rolls)
    num_to_check = sorted_rolls[2]

    # count number of times this number appears
    total = 0
    for num in rolls:
        if num == num_to_check:
            total += 1

    # determine result
    if total < 3:
        return ""
    if total == 3:
        for i in range(3):
            sorted_rolls.remove(num_to_check)
        if sorted_rolls[0] == sorted_rolls[1]:      # check if other two numbers are a pair
            return "full house!"
        else:
            return "3-of-a-kind."
    if total == 4:
        return "4-of-a-kind!"
    if total == 5:
        return "YAHTZEE!"
    
def straight(rolls):
    '''
    Checks if the player rolled a small or large straight
    '''
    # all straights need 3 and 4
    if 3 in rolls and 4 in rolls:
        # all large straights need 2 and 5
        if 2 in rolls and 5 in rolls:
            if 1 in rolls or 6 in rolls:
                return "large straight!"
            else:
                return "small straight."
        elif (1 in rolls and 2 in rolls) or (5 in rolls and 6 in rolls):
            return "small straight."
    
    return ""

res = of_a_kind(kept_nums) + straight(kept_nums)
if res == "":
    print("Sorry, try again!")
else:
    print("Horray! You rolled a " + res)