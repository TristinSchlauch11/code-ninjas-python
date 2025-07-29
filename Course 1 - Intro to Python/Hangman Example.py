word_to_guess = "sensei"
answer = list(word_to_guess)
guesses = []
lives_left = 7

def guessed():
    for letter in answer:
        if letter not in guesses:
            return False
    # all letters in answer have been guessed
    return True

def print_word_so_far():
    message = ""
    for letter in answer:
        if letter in guesses:
            message = message + letter + " "
        else:
            message = message + "_ "
    print(message)

while lives_left > 0 and not guessed():
    # print word so far and lives left on screen
    print_word_so_far()
    print("Lives Left: " + str(lives_left))

    # ask for a letter
    letter = input("Please guess a lowercase letter >> ")
    if not letter.isalpha() or not letter.islower() or len(letter) != 1:
        print("Not a valid letter!")
        continue

    # check if it has been guessed
    if letter in guesses:
        print("You already guessed that letter!")
    # if not, add it to guessed letters
    else:
        guesses.append(letter)
        if letter in answer:
            print("Nice! You guessed a letter!")
        # if letter not in answer, lose a life
        else:
            print("Sorry! That letter isn't in the word.")
            print("You lost a life.")
            lives_left = lives_left - 1

if lives_left > 0:
    print("Congratulations! You guessed the word " + word_to_guess + "!")
else:
    print("Sorry, you ran out of lives! The word was " + word_to_guess + ".")