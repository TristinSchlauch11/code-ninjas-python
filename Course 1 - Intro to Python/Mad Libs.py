# In this project, we will be creating a Mad Libs story that you can share with your friends! If you don't know, Mad
# Libs are a story that has some words missing! You are asked to fill in the blanks with specific words or numbers,
# then you will have a silly story! We are going to code a Mad Lib by asking the player to type in specific words, then
# we'll print our story filled in with the words the player typed in onto the screen for the player to read!

# Step 1:
# [O] Use a print statement to print a welcome message to the player.
# Remember to put your message in "quotation marks"!

print("Welcome to Mad Libs!")

# Step 2:
# [] Use the input function to ask the player to type in at least 5 types of words or numbers. Be descriptive about
# what type of word or number they need to type in and remember to include spaces at the end of your inputs!
# [] Store each of these inputted values into different variables that you can use later in your program.

name = input("name ")
verb = input("verb ")
colour = input("colour ")

#### DO NOT CHANGE THIS CODE ####
print("")
#################################

# Step 3:
# [] Use print statements and string concatenation to print your Mad Libs story!
# Remember to include spaces between the words that you are joining together!

print("Our hero " + name + " visited my grandmother today.")