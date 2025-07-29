# print a welcome message
print("Welcome to Mad Libs!")

# create the inputs
place = input("Enter the name of a city or town >> ")
name = input("Enter your name >> ")
num1 = input("Enter a number bigger than 20 >> ")
food = input("Enter your favourite food >> ")
adj1 = input("Enter an 'ly' adjective >> ")
anim1 = input("Enter a strange animal name >> ")
anim2 = input("Enter another strange animal name >> ")
adj2 = input("Enter another adjective >> ")
verb = input("Enter a verb >> ")
villian = input("Enter the name of a villian >> ")
num2 = input("Enter another number bigger than 20 >> ")

# print the Mad Libs story!
print("")
print("It was a beautiful day in the Land of " + place + " yesterday.")
print("Somehow, " + name + " managed to eat over " + num1 + " helpings")
print("of " + food + " for breakfast! Then, they " + adj1 + " got")
print("dressed and ran out the door, hoping they wouldn't be late for")
print("the bus. But then, a wild " + anim1 + " appeared and " + name)
print("had to fight it Pokemon style! " + name + " shouted 'Go " + anim2 + "!'")
print("It was a " + adj2 + " fight, but " + anim2 + " barely won, finishing off")
print(anim1 + " with their signature " + verb + " move. Just then, the bus turned")
print("around the corner and stopped in front of " + name + ". They got on,")
print("but had to sit beside " + villian + " on the way to school! Too bad")
print("it was over " + num2 + " minutes away!")

# print a "the end" message
print("The end!")