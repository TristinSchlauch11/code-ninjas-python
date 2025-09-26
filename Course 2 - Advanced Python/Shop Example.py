prices = {'apple' : 1.50, 'orange' : 2.00, 'banana' : 0.75}

def print_all_items():
    for item in prices.keys():
        print(item)

# changing prices dictionary
def add_item(new_item, price):
    if new_item in prices.keys():
        print("That item already exists!")
    else:
        prices[new_item] = price
        print("Item added!")

def remove_item(item):
    if item in prices.keys():
        prices.pop(item)
        print("Item removed!")
    else:
        print("That item doesn't exist!")

def change_price(item, new_price):
    if item in prices.keys():
        prices[item] = new_price
        print("Price updated!")
    else:
        print("That item doesn't exist!")


# managing items menu
def manage():
    all_managed = False
    while not all_managed:
        print("\n")
        print("Enter 'add' to add a new item.")
        print("Enter 'remove' to remove an existing item.")
        print("Enter 'edit' to change the price of an existing item.")
        print("Enter 'list' to print a list of all items we have.")
        print("Enter 'done' when you're finished managing your items.")

        sel = input("Please select an option! >> ")
        if sel == "done":
            all_managed = True
        elif sel == "add":
            item = input("What is the item you want to add? >> ")
            price = float(input("What price do you want this item to be? >> "))
            add_item(item, price)
        elif sel == "edit":
            item = input("What is the item you want to edit? >> ")
            price = float(input("What price do you want this item to be? >> "))
            change_price(item, price)
        elif sel == "remove":
            item = input("What is the item you want to remove? >> ")
            remove_item(item)
        elif sel == "list":
            print_all_items()
        else:
            print("Invalid entry...")


# customer shopping function
def scan():
    print("\n")
    # scan all items
    all_scanned = False
    items = []
    while not all_scanned:
        item = input("Type your next item, type 'list' to see all items, or type 'done' when done >> ")
        if item == "done":
            all_scanned = True
        elif item == "list":
            print_all_items()
        elif item in prices.keys():
            items.append(item)
        else:
            print("We don't have that item...")
    
    # calculate price of all items
    for i in range(len(items)):
        item = items[i]             # get item name
        items[i] = prices[item]     # get item price

    total = sum(items)
    print(f"Thanks for shopping! Your total is ${total:.2f}!")

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
    if sel == "scan":
        scan()
    elif sel == "manage":
        manage()
    elif sel == "done":
        done = True
    else:
        print("Invalid entry...")