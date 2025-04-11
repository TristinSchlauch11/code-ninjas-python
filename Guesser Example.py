import random

num_to_guess = random.randint(1, 100)
guesses = []

def print_guesses():
    if len(guesses) == 0:
        print("You've made no guesses!")
        return
    for guess in guesses:
        if guess > num_to_guess:
            print(str(guess) + " was too high")
        else:
            print(str(guess) + " was too low")

print("Welcome! Try to guess the number between 1 and 100, and I'll tell you if it's higher or lower!")

while num_to_guess not in guesses:
    next_guess = int(input("Enter your next guess, or view all guesses by entering 0 >> "))
    if next_guess == 0:
        print_guesses()
    elif next_guess < 0 or next_guess > 100:
        print("Guess a number between 1 and 100!")
    else:
        guesses.append(next_guess)
        if next_guess == num_to_guess:
            print("Congratulations! You guessed the number!")
            print("It took you " + str(len(guesses)) + " tries to guess the number " + str(num_to_guess))
        elif next_guess > num_to_guess:
            print("That number is too high.")
        else:
            print("That number is too low.")