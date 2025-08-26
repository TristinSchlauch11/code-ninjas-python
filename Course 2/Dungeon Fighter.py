# Welcome to your final project! In this project, you will be coding a turn-based combat game!
# In this game, you will play the role of a wizard fighting a series of monsters. The farther
# you get, the harder the monsters get! You have the ability to use your magic to try and make
# the fight easier for you, while the monster will do a random move each turn. To make the game
# work, you will need two classes: Player and Monster. A lot of the code has already been done
# for you, so you just need to fill in the rest!


# Step 1
# The monster will do random moves, so we'll need the random module
# [] Import the random module



# This is the class that will define the attributes and methods that our Hero will use
class Player():
    # Step 2
    # First, we need to create the __init__ method that will define all of the attributes that
    # the Player will use. Remember to use the word "self" as a parameter of the __init__ function
    # and in front of all of the attributes you use.
    # [] Set hit_points to 200
    # [] Set max_hit_points to 200
    # [] Set magic to 0
    # [] Set max_magic to 200
    # [] Set damage to 30
    # [] Set healing to 50
    # [] Set power_inc to 1.5
    # [] Set defense to 0.75
    # [] Set powered_up to False
    # [] Set defending to False
    # [] Set cursed to False
    # [] Set actions to this dictionary:
    actions = {
            "attack" : "Deals 30 damage to the monster (before power ups)",
            "heal" : "Uses 70 magic, Restores 50 hit points",
            "power" : "Uses 50 magic, Increases your next attack by 50%",
            "defend" : "Uses 50 magic, Reduces the next damage you take by 25%",
            "stun" : "Uses 90 magic, Removes all effects applied to the monster",
            "magic" : "Increases your magic by 40" 
        }

    # Phew! That was a lot of attributes, but we got through it. Now that all of our attributes
    # are defined, we need to give our class some methods to use. Some of them have already been
    # created, so we'll tell you when we need you to create a method.

    # gameplay methods
    # This method prints your health and magic, as well as any modifiers currently applied to you
    def print_stats(self):
        print("\nYour Stats and Effects:")
        print("Health: " + str(self.hit_points) + "/" + str(self.max_hit_points))
        print("Magic: " + str(self.magic) + "/" + str(self.max_magic))
        if self.powered_up: print("You're powered up!")
        if self.defending: print("You're defending!")
        if self.cursed: print("You're cursed!")

    # Step 2
    # This method, get_available_moves, will get a list of all the actions that the hero can do
    # at the start of the turn. You need to finish this method!
    def get_available_moves(self, monster):
        # [] You can always attack, so set the 'moves' list to a list with only one element, "attack"
        moves = []              # you can always attack

        # [] Now, if you are not cursed, there are other actions that you can do.
        #    Start an if statement below all of these comments
        #   [] If our magic is not equal to our max_magic, we can get more magic. So, append "magic" 
        #      to the moves list.
        #   [] If our magic is at least 70 and our hit_points is not equal to our max_hit_points, 
        #      we can heal. So, append "heal" to the moves list.
        #   [] If our magic is at least 50 and we are not powered_up, we can power up! So, append
        #      "power" to the moves list.
        #   [] If our magic is at least 50 and we are not defending, we can defend! So, append
        #      "defend" to the moves list.
        # There is also one more move that we could do that has already been coded for.
        # If our magic is at least 90 and the monster is either powered up or defending, we can stun
        # it. So, we'll add stun to the moves list.



            # DO NOT CHANGE
            if self.magic >= 90 and (monster.powered_up or monster.defending):
                moves.append("stun")


        # [] Finally, you need to return the moves list!


    # This method will print all of the moves that the hero can do at the start of the turn
    def print_moves(self, moves_list):
        print("\nYour available moves this turn are:")
        for move in moves_list:
            print(move + ": " + self.actions[move])

    # This method will do a specific action depending on what action the player selected
    def do_action(self, action, monster):
        if action == "attack":
            self.attack(monster)
            self.cursed = False
        elif action == "heal":
            self.heal()
        elif action == "power":
            self.power_up()
        elif action == "defend":
            self.defend()
        elif action == "stun":
            self.stun(monster)
        elif action == "magic":
            self.magic_up()

    # Step 3
    # This method, play_turn, goes through the steps of having the player take their turn. Here,
    # we want to print the players stats, the monsters stats, then have the player select a
    # valid move and perform it. The code where the player selects their next action has already
    # been filled in, you just need to do the rest!
    def play_turn(self, monster):
        # [] Print the player's stats by calling the PLayer's (self) print_stats method
        # [] Print the monster's stats by calling the monster's print_stats method
        # [] Get the list of moves that they player can do by calling the get_available_moves method
        #    Use 'monster' as the argument, and store the result in a variable called 'moves'
        # [] Print all of these moves by calling the Player's print_moves method
        #    Use the 'moves' list as the argument for the method



        # get action from player
        action = ""
        while action not in moves:
            action = input("Please select your next action >> ")
            if action not in moves:
                if action in self.actions:
                    print("You can't do that action right now!")
                else:
                    print("That's not a valid move!")

        # [] Finally, after the player selects their move, you need to do it! Call the Player's
        #    do_action function, using the 'action' and 'monster' variables as arguments



    # Step 4
    # Now, we need to define some more methods. These methods will be the 'actions' that are hero
    # can do on each turn. They will be attack, heal, power_up, defend, stun, and magic_up

    # [] Define an attack function that uses 2 parameters: self and enemy
    #    [] If the Player is powered up, call the enemy's take_damage function
    #    [] Multiply the Player's damage and power_inc numbers together and use this as the argument
    #    [] Also, set the Player's powered_up Boolean to False
    #    [] Otherwise, call the enemy's take_damage function and use the Player's damage as the argument



    # [] Define a heal function that uses only the self parameter
    # [] Decrease the Player's magic attribute by 70
    # [] Set the Player's hit_points to the MINIMUM of:
    #       adding the Player's healing attribute to their hit_points
    #   and the Player's max_hit_points attribute


    
    # [] Define a power_up function that uses only the self parameter
    # [] Decrease the Player's magic attribute by 50
    # [] Set the Player's powered_up attribute to True



    # [] Define a defend function that uses only the self parameter
    # [] Decrease the Player's magic attribute by 50
    # [] Set the Player's defending attribute to True



    # [] Define a stun function that uses 2 parameters: self and enemy
    # [] Decrease the Player's magic attribute by 90
    # [] Call the enemy's get_stunned method   
    


    # [] Define a magic_up function that uses only the self parameter
    # [] Set the Player's magic attribute to the MINIMUM of:
    #       increasing the Player's magic attribute by
    #   AND the Player's max_magic attribute


    
    # monster method effects
    def take_damage(self, damage):
        if self.defending:
            self.hit_points = max(int(self.hit_points - (damage * self.defense)), 0)
            self.defending = False
        else:
            self.hit_points = max(int(self.hit_points - damage), 0)

    # [] Define a get_cursed function that uses only the self parameter
    # [] Set the Player's cursed attribute to True



    # [] Define a defeated function that uses only the self parameter
    # [] Return a Boolean that is True if the Player has 0 hit_points, and False otherwise

    

# Step 5
# Horray! We finished the Player class! Now, we need to code the Monster class. A lot of the stuff
# that we need to do to create the Monster class is the same as the Player class, so most of it is
# already filled in. Check to see if there are any steps that still need to be done in the class!
class Monster():

    # [] This __init__ method will make the monster harder to fight when the Monster's level gets higher!
    #    But, it doesn't work right! Can you fix it by adding a level parameter to the method?
    def __init__(self):
        # health
        self.max_hit_points = 50 + 10 * level
        self.hit_points = 50 + 10 * level

        # fighting stats
        self.damage = 10 + 5 * level
        self.healing = 20 + 5 * level
        self.power_inc = 1.05 + 0.05 * level
        self.defense = 0.90 - 0.05 * level

        # modifiers
        self.powered_up = False
        self.defending = False

        # actions dictionary
        self.actions = {
            "attack" : "Deals " + str(self.damage) + " damage to you (before power ups)",
            "heal" : "Restores " + str(self.healing) + " hit points",
            "power" : "Increases the monster's next attack by " + str(round((self.power_inc - 1) * 100)) + "%",
            "defend" : "Reduces the next damage the monster takes by " + str(round((1 - self.defense) * 100)) + "%",
            "curse" : "Prevents you from using or gaining magic on your next turn"
        }

        # Whenever we spawn a new monster, we want to print all of its moves for the hero to see.
        # [] Call the Monster's print_all_move function




    # gameplay methods
    # prints health and modifiers currently applied to the monster
    def print_stats(self):
        print("\nMonster Stats and Effects:")
        print("Monster Health: " + str(self.hit_points) + "/" + str(self.max_hit_points))
        if self.powered_up: print("The monster is powered up!")
        if self.defending: print("The monster is defending!")
    
    # prints all of the Monster's moves
    def print_all_moves(self):
        print("\nA new monster appeared! It has these moves!")
        for move in self.actions:
            print(move + ": " + self.actions[move])

    # gets all moves that the Monster is able to do this turn
    def get_available_moves(self, hero):
        moves = ["attack", "curse"]     # monster can always attack and curse
        if self.hit_points != self.max_hit_points:
            moves.append("heal")
        if not self.powered_up:
            moves.append("power")
        if not self.defending:
            moves.append("defend")
        return moves

    # performs an action
    def do_action(self, action, hero):
        if action == "attack":
            self.attack(hero)
            self.cursed = False
        elif action == "heal":
            self.heal()
        elif action == "power":
            self.power_up()
        elif action == "defend":
            self.defend()
        elif action == "curse":
            self.curse(hero)

    # In this play_turn method, the Monster takes their turn. It is just a little bit different
    # than the Player's play_turn method because the Monster will choose their action randomly
    def play_turn(self, hero):
        # [] Get the list of moves that the monster can do by calling the get_available_moves method
        #    Use 'hero' as the argument, and store the result in a variable called 'moves'
        # [] Use the random module's choice function to randomly choose an action from the 'moves' list
        #    and assign it to a variable called 'action'
        # [] Print the action that the monster used so that the hero knows what the monster did
        


        self.do_action(action, hero)

    # monster methods
    def attack(self, hero):
        if self.powered_up:
            hero.take_damage(self.damage * self.power_inc)
            self.powered_up = False
        else:
            hero.take_damage(self.damage)

    def heal(self):
        self.hit_points = min(self.hit_points + self.healing, self.max_hit_points)

    def power_up(self):
        self.powered_up = True

    def defend(self):
        self.defending = True

    # [] Define a curse function that uses 2 parameters: self and hero
    # [] Call the hero's get_cursed method   



    # hero method effects
    def take_damage(self, damage):
        if self.defending:
            self.hit_points = max(int(self.hit_points - (damage * self.defense)), 0)
            self.defending = False
        else:
            self.hit_points = max(int(self.hit_points - damage), 0)

    # [] Define a get_stunned function that uses only the self parameter
    # [] Set the Monster's powered_up Boolean to False
    # [] Set the Monster's defending Boolean to False
    
    def defeated(self):
        return self.hit_points == 0

# Step 6
# We have both classes set up! Now, we just need to write the code that runs our game!
# [] Construct a Player and assign it to a variable called 'hero'
# [] Construct a Monster whose level is 0 and assign is to a variable called 'enemy'
# [] Set a 'points' variable to the number 0.



# [] Use a while loop to run the keep while the hero is not defeated
#    [] On every turn, let the hero play their turn by calling the hero's play_turn method. Use 'enemy' as the argument
#    [] After the player's turn, if the enemy is defeated we need to:
#         [] Increase the score by 1
#         [] Set the enemy to a new Monster that uses 'points' as its level
#    [] Otherwise, let the monster play their turn by calling the enemy's play_turn method. Use 'hero' as the argument



# This will print when the game ends!
print("Oh no! You died! You scored " + str(points) + " points!")