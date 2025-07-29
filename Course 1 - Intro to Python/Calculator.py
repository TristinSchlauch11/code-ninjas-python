# In this final project, we will be building a calculator! Our calculator will be able to add, subtract, multiply, 
# and divide as many times as we want until we want to finish the calculation. We can also restart our calculation
# by pressing the "c" button.

# Step 1:
# First, we need to create a function that can calculate! We'll call this function in our main program to do math for us!

# [] Start by defining a function called 'calculate'. This function needs to have 3 parameters: a number 'x', another
# number 'y', and a string called 'operation'
# [] Next, we need to use an if-elif block to decide which mathematical operation we need to perform:
#   [] If operation is "+", we should add x and y together and return the result
#   [] If operation is "-", we should subtract y from x and return the result
#   [] If operation is "*", we should multiply x by y and return the result
#   [] If operation is "/", we should divide x by y and return the result
# HINT: If we code the rest of the project right, we should't need to use 'else' here



# Step 2:
# Now, we need to build our calculator! First, we'll set up some variables that we'll use throughout the program.

# [] Use an input function to ask the player to enter the first number of their calculation and store it in a variable
# called 'answer'
# [] We also need to define a Boolean variable called 'finished' and set it to False



# Step 3:
# Since we need to do an unknown amount of calculations, we need to use a while loop. We'll use the 'finished'
# Boolean variable to track when we need to end the loop.

# [] Write the first line of the while loop. We will continue to operate the loop until 'finished' is True.
# [] Inside the loop, we will start by asking the player to enter the next operation, "=" to finish, or "c" to restart
# Do this with an input statement, and store the input in a variable called 'op'.



# Step 4:
# Next, we need to check what the player typed in and decide what to do next. For this, we will need an if-elif-else
# statement.

# [] First, if the player entered one of the four operations (+, -, *, /), they want to do another calculation! 
# HINT: How can we check to see if 'op' is any one of '+', '-', '*', or '/'?
#   [] Use an input statement to ask the player for the next number, and store it in a variable called 'number'. 
#   [] Call the 'calculate' function using 'answer', 'number', and 'op' as the parameters. Store this result back into 
#   the 'answer' variable.
# [] If the player entered '=', they are done calculating! Print the 'answer' variable, then set the 'finished' variable 
# to True. This will end the loop.
# [] If the player entered 'c', they want to restart. Print a restart message on the screen, then ask the player to enter
# the first number again. Store this number in the 'answer' variable.
# [] If the player entered anything else, they entered something wrong! Print "Invalid operation!" on the screen to let 
# the player know that they have made a mistake.


