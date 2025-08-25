import random

rolls_left = 3
kept_nums = []

def roll(dice_to_roll):
    # init empty rolls list
    rolls = []

    # roll 6-sided die for every die to roll
    for i in range(dice_to_roll):
        roll = random.randint(1,6)
        rolls.append(roll)

    # return list of rolled numbers
    return rolls

def pick_dice(nums):
    done = False
    keep = []

    while not done:
        print("You rolled these numbers:")
        print(nums)
        print("Please pick which ones you want to keep.")

        for num in nums:
            sel = input("Type 'y' to keep the number " + str(num) + " >> ")
            if sel.lower() == "y":
                keep.append(num)
        
        print("You rolled these numbers:")
        print(nums)
        print("You want to keep these numbers:")
        print(keep)

        check = input("Type 'y' if this is correct >> ")
        if check.lower() == "y":
            return keep
        else:
            keep = []

while rolls_left > 0 and len(kept_nums) < 5:
    # roll the dice and remove a roll
    rolled_nums = roll(5 - len(kept_nums))
    all_nums = kept_nums + rolled_nums
    rolls_left = rolls_left - 1

    # pick the dice to keep
    if rolls_left == 0:
        kept_nums = all_nums
    else:
        kept_nums = pick_dice(all_nums)

print("On your final roll, you rolled these numbers:")
print(kept_nums)

### DO NOT CHANGE THIS CODE ###
def of_a_kind(rolls):
    '''
    Checks if the player rolled a 3-of-a-kind, 4-of-a-kind, or a Yahtzee
    Also checks for a full house
    '''
    # sort numbers
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