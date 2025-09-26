# Welcome to our second project! In this project, we will be creating a program that acts like
# a shopkeeper's computer! On this computer, we use a dictionary to store the prices of all of
# the items that are sold at the shop. We can add and remove items, and change the prices of 
# existing items. We can also scan a bunch of items in our store and find the total price for
# a customer's order!

# Step 1
# First, we need to define an initial dictionary that holds some of the prices of our items
# [] Define a dictionary called prices that uses the store items (strings) as keys and their 
#    prices (floats) as the value. Use at least 3 items.



# Step 2:
# Now, you're going to define 4 functions that use the prices dictionary and change its contents
# [] Define a function called print_all_items() that prints all items in the store.
#    If you want, you can also print the prices of the items.
# [] Define a function called add_item(new_item, price) that adds the new item to the store 
#    with the given price. 
#    [] But, if the item is already a key in the prices dictionary, we should ignore this item 
# [] Define a function called change_item(item, new_price) that changes the price of the given 
#    item to the new given price. 
#    [] But, if the item is not a key in the prices dictionary, we should ignore this change 
# [] Define a function called remove_item(item) that removes the item from the store
#    [] But, if the item is not a key in the prices dictionary, we should ignore this change 



# Step 3:
# Next, we're going to start creating the computer menus. The first one that we'll make is the 
# managing items menu. From this menu, we can add and remove items, or change item prices. Some
# of the code is already there, your job is to create an if-elif-else statement to decide what
# to do depending on what input the user provides on this menu. DO NOT CHANGE ANY CODE THAT IS 
# ALREADY HERE! 
def manage():
    all_managed = False
    while not all_managed:
        # printing the menu options
        print("\n")
        print("Enter 'add' to add a new item.")
        print("Enter 'remove' to remove an existing item.")
        print("Enter 'edit' to change the price of an existing item.")
        print("Enter 'list' to print a list of all items we have.")
        print("Enter 'done' when you're finished managing your items.")

        # asking the user for input 
        sel = input("Please select an option! >> ")

        # Put your if-elif-else statement here!
        # Don't forget to change the price inputs to floats!
        # [] If the input is 'done', you should exit the menu by changing a variable. Which one?
        # [] If the input is 'add', we will add an item!
        #    [] Use 2 input statements to get the new item and its price, then call the add_item function
        # [] If the input is 'edit', we will change an item's price!
        #    [] Use 2 input statements to get the item and its new price, then call the change_item function
        # [] If the input is 'remove', we will remove an item!
        #    [] Use 2 input statements to get the item and its price, then call the remove_item function
        # [] If the input is 'list', we want to print all the items!
        #    [] Call the print_all_items function
        # [] If the input is anything else, tell the user they provided an invalid entry



# Step 4
# Now, we'll make the scanning menu where you will scan a bunch of items, then compute the total
# price of all the items in the order. Again, some of the function is already defined, you just
# need to finish it!
# customer shopping function
def scan():
    print("\n")
    all_scanned = False
    items = []      # list to store all the items that get scanned

    while not all_scanned:
        item = input("Type your next item, type 'list' to see all items, or type 'done' when done >> ")
        
        # Here, you need to create an if-elif-else statement to decide what to do depending on user input
        # [] If the input is 'done', you should exit the menu by changing a variable. Which one?
        # [] If the input is 'list', we want to print all the items! Call the print_all_items function
        # [] If the input is an item, append it to the items list
        # [] If the input is anything else, tell the user they provided an invalid entry
        

    
    # Now that all the items got scanned, we need to find the total price! To do this, we're going to
    # replace each item in the items list with its price, then use the sum function to add all the prices
    # together. Below, you need to code a for loop that changes the items to their prices
    # [] Define a for loop that uses a RANGE function that will go over all elements in the items list
    #    [] Use list indexing to get the item at each index in the items list
    #    [] Change each item in the list to be the price of the item



    # add up all prices and print total price
    total = sum(items)
    print(f"Thanks for shopping! Your total is ${total:.2f}!")

# Step 5
# This is it! Now, you just need to code the main menu! From this menu, you can access the scanning
# menu and the managing menu. Most of the code is there, you just need to do the if-elif-else statement
# that decides what to do depending on the user's input. DO NOT CHANGE ANY CODE THAT IS ALREADY HERE!
done = False
while not done:
    # print intro message and options
    print("\n")
    print("Welcome to Python Shop!")
    print("Enter 'manage' to manage your items and prices.")
    print("Enter 'scan' to start scanning a customer's items.")
    print("Enter 'done' to exit the computer.")

    # get selection
    sel = input("Please select an option! >> ")

    # Here, you need to create an if-elif-else statement to decide what to do depending on user input
    # [] If the input is 'done', you should exit the menu by changing a variable. Which one?
    # [] If the input is 'scan', we want to scan a customer's items! Call the scan function
    # [] If the input is 'manage', we want to manage our items! Call the manage function
    # [] If the input is anything else, tell the user they provided an invalid entry


