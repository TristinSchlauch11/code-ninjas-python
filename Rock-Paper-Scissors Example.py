import random

# set up
ply_input = ""
answers = ["rock", "paper", "scissors"]

# ask user for input
# kids will NOT be expected to code the while loop yet
while ply_input not in answers:
    ply_input = input("Please enter 'rock', 'paper', or 'scissors' >> ")
    if ply_input not in answers:
        print("That's not a valid input!")

# get computer input
# kids will NOT be expected to generate a random number
cpu_num = random.randint(0, 2)
cpu_input = answers[cpu_num]
print("The computer selected " + cpu_input)

# determines the outcome
if ply_input == "rock":
    if cpu_input == "rock":
        print("It's a draw!")
    elif cpu_input == "paper":
        print("Paper covers rock. You lose.")
    else:
        print("Rock smashes scissors. You win!")
elif ply_input == "paper":
    if cpu_input == "rock":
        print("Paper covers rock. You win!")
    elif cpu_input == "paper":
        print("It's a draw!")
    else:
        print("Scissors cuts paper. You lose.")
else:
    if cpu_input == "rock":
        print("Rock smashes scissors. You lose.")
    elif cpu_input == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("It's a draw!")