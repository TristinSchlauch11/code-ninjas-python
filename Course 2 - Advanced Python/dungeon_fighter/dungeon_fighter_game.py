# Welcome to your final project! In this project, you will be coding a turn-based combat game!
# In this game, you will play the role of a wizard fighting a series of monsters. The farther
# you get, the harder the monsters get! You have the ability to use your magic to try and make
# the fight easier for you, while the monster will do a random move each turn. To make the game
# work, you will need two classes: Player and Monster. A lot of the code has already been done
# for you, so you just need to fill in the rest!

# Step 1
# The monster will do random moves, so we'll need the random module
# [] Import the random module
import random

# This is the class that will define the attributes and methods that our Hero will use
class Player():
    # Step 2
    # Most of our attributes have already been defined! Check to see if there are any left!
    def __init__(self):
        # health
        # [] Set hit_points to 200
        # [] Set max_hit_points to 200
        self.hit_points = 200
        self.max_hit_points = 200

        # magic
        # [] Set magic to 80
        # [] Set max_magic to 200
        self.magic = 80
        self.max_magic = 200

        # fighting stats
        self.damage = 30
        self.healing = 50
        self.power_inc = 1.5
        self.defense = 0.75

        # modifiers
        self.powered_up = False
        self.defending = False
        self.cursed = False

        # actions dictionary
        self.actions = {
            "attack" : "Deals 30 damage (before power ups)",
            "heal" : "(-70 MP) Restores 50 HP",
            "power" : "(-50 MP) Increases next attack by 50%",
            "defend" : "(-50 MP) Reduces next damage you take by 25%",
            "stun" : "(-90 MP) Removes all effects from monster",
            "magic" : "Increases your MP by 40"
        }

    # gameplay methods
    # This method, get_available_moves, will get a list of all the actions that the hero can do
    # at the start of the turn.
    def get_available_moves(self, monster):
        moves = ["attack"]              # you can always attack
        if not self.cursed:             # you can only use magic if not cursed
            if self.magic != self.max_magic:
                moves.append("magic")
            if self.magic >= 90 and (monster.powered_up or monster.defending):
                moves.append("stun")
            if self.magic >= 70 and self.hit_points != self.max_hit_points:
                moves.append("heal")
            if self.magic >= 50 and not self.powered_up:
                moves.append("power")
            if self.magic >= 50 and not self.defending:
                moves.append("defend")
        return moves

    # This method will print all of the moves that the hero can do at the start of the turn
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

    # hero methods
    # Step 3
    # Next, we need to define some more methods. These methods will be the 'actions' that are hero
    # can do on each turn. They will be attack, heal, power_up, defend, stun, and magic_up

    # This is our attack method, which will be called when our Hero attacks the Monster
    def attack(self, enemy):
        if self.powered_up:
            enemy.take_damage(self.damage * self.power_inc)
            self.powered_up = False
        else:
            enemy.take_damage(self.damage)

    # Next, we'll need a heal method! This will restore our Hero's health!
    # [] Define a heal method that uses only the self parameter
    # [] Decrease the Player's magic attribute by 70
    # [] Set the Player's hit_points to the MINIMUM of:
    #       - adding the Player's healing attribute to their hit_points, and
    #       - the Player's max_hit_points attribute
    def heal(self):
        self.magic = self.magic - 70
        self.hit_points = min(self.hit_points + self.healing, self.max_hit_points)


    # Next, you need a power_up method! This will make the Hero's next attack stronger!
    # [] Define a power_up method that uses only the self parameter
    # [] Decrease the Player's magic attribute by 50
    # [] Set the Player's powered_up attribute to True
    def power_up(self):
        self.magic = self.magic - 50
        self.powered_up = True


    # Next, you need a defend method! This reduces the damage of the Monster's next attack
    # [] Define a defend method that uses only the self parameter
    # [] Decrease the Player's magic attribute by 50
    # [] Set the Player's defending attribute to True
    def defend(self):
        self.magic = self.magic - 50
        self.defending = True


    # Next, we'll create a method that can stun the enemy!
    # [] Define a stun method that uses 2 parameters: self and enemy
    # [] Decrease the Player's magic attribute by 90
    # [] Call the enemy's get_stunned method
    def stun(self, enemy):
        self.magic = self.magic - 90
        enemy.get_stunned()


    # This is a method that increases our Hero's magic
    def magic_up(self):
        self.magic = min(self.magic + 40, self.max_magic)

    # monster method effects
    def take_damage(self, damage):
        if self.defending:
            self.hit_points = max(int(self.hit_points - (damage * self.defense)), 0)
            self.defending = False
        else:
            self.hit_points = max(int(self.hit_points - damage), 0)

    # This a function that will get called when the Monster curses our hero!
    # [] Define a get_cursed function that uses only the self parameter
    # [] Set the Player's cursed attribute to True
    def get_cursed(self):
        self.cursed = True


    # Finally, we need a method to check if our Hero was defeated!
    # [] Define a defeated function that uses only the self parameter
    # [] Return a Boolean that is True if the Player has 0 hit_points, and False otherwise
    def defeated(self):
        if self.hit_points == 0:
            return True
        else:
            return False


# Step 4
# Horray! We finished the Player class! Now, we need to code the Monster class. A lot of the stuff
# that we need to do to create the Monster class is the same as the Player class, so most of it is
# already filled in. Check to see if there are any steps that still need to be done in the class!
class Monster():

    # [] This __init__ method will make the monster harder to fight when the Monster's level gets higher!
    #    But, it doesn't work right! Can you fix it by adding a level parameter to the method?
    def __init__(self, level):
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
            "heal" : "Restores " + str(self.healing) + " HP",
            "power" : "Increases next attack by " + str(round((self.power_inc - 1) * 100)) + "%",
            "defend" : "Reduces the next damage taken by " + str(round((1 - self.defense) * 100)) + "%",
            "curse" : "You cannot use/gain magic on your next turn"
        }

    # gameplay methods
    # This method will return a list of actions that the monster can do at the start of its turn
    def get_available_moves(self, hero):
        moves = ["attack", "curse"]     # monster can always attack and curse
        if self.hit_points != self.max_hit_points:
            moves.append("heal")
        if not self.powered_up:
            moves.append("power")
        if not self.defending:
            moves.append("defend")
        return moves

    # Next, we need a method that will randomly pick the Monster's next move!
    # [] Define a pick_move method that has 2 parameters: self and hero
    # [] Get the list of moves that the monster can do by calling the get_available_moves method
    #    Use 'hero' as the argument, and store the result in a variable called 'moves'
    # [] Use the random module's choice function to randomly choose an action from the 'moves' list
    #    and assign it to a variable called 'action'
    # [] Return the action
    def pick_move(self, hero):
        moves = self.get_available_moves(hero)
        action = random.choice(moves)
        return action

    # This method lets the monster perform an action
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

    # Next, we need a method that can curse our Hero!
    # [] Define a curse function that uses 2 parameters: self and hero
    # [] Call the hero's get_cursed method
    def curse(self, hero):
        hero.get_cursed()


    # hero method effects
    def take_damage(self, damage):
        if self.defending:
            self.hit_points = max(int(self.hit_points - (damage * self.defense)), 0)
            self.defending = False
        else:
            self.hit_points = max(int(self.hit_points - damage), 0)

    # Finally, we need a method that let's the Monster get stunned!
    # [] Define a get_stunned function that uses only the self parameter
    # [] Set the Monster's powered_up Boolean to False
    # [] Set the Monster's defending Boolean to False
    def get_stunned(self):
        self.powered_up = False
        self.defending = False


    def defeated(self):
        return self.hit_points == 0
