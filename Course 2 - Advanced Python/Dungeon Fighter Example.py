import random

class Player():
    def __init__(self):
        # health
        self.max_hit_points = 200
        self.hit_points = 200

        # magic
        self.max_magic = 200
        self.magic = 0

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
            "attack" : "Deals 30 damage to the monster (before power ups)",
            "heal" : "Uses 70 magic, Restores 50 hit points",
            "power" : "Uses 50 magic, Increases your next attack by 50%",
            "defend" : "Uses 50 magic, Reduces the next damage you take by 25%",
            "stun" : "Uses 90 magic, Removes all effects applied to the monster",
            "magic" : "Increases your magic by 40" 
        }

    # gameplay methods
    def print_stats(self):
        print("\nYour Stats and Effects:")
        print("Health: " + str(self.hit_points) + "/" + str(self.max_hit_points))
        print("Magic: " + str(self.magic) + "/" + str(self.max_magic))
        if self.powered_up: print("You're powered up!")
        if self.defending: print("You're defending!")
        if self.cursed: print("You're cursed!")

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

    def print_moves(self, moves_list):
        print("")
        print("Your available moves this turn are:")
        for move in moves_list:
            print(move + ": " + self.actions[move])

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

    def play_turn(self, monster):
        # print all start-of-turn stuff
        self.print_stats()
        monster.print_stats()
        moves = self.get_available_moves(monster)
        self.print_moves(moves)

        # get action from player
        action = ""
        while action not in moves:
            action = input("Please select your next action >> ")
            if action not in moves:
                if action in self.actions:
                    print("You can't do that action right now!")
                else:
                    print("That's not a valid move!")

        # do action
        self.do_action(action, monster)

    # hero methods
    def attack(self, enemy):
        if self.powered_up:
            enemy.take_damage(self.damage * self.power_inc)
            self.powered_up = False
        else:
            enemy.take_damage(self.damage)

    def heal(self):
        self.magic = self.magic - 70
        self.hit_points = min(self.hit_points + self.healing, self.max_hit_points)

    def power_up(self):
        self.magic = self.magic - 50
        self.powered_up = True

    def defend(self):
        self.magic = self.magic - 50
        self.defending = True

    def stun(self, enemy):
        self.magic = self.magic - 90
        enemy.get_stunned()

    def magic_up(self):
        self.magic = min(self.magic + 40, self.max_magic)
    
    # monster method effects
    def take_damage(self, damage):
        if self.defending:
            self.hit_points = max(int(self.hit_points - (damage * self.defense)), 0)
            self.defending = False
        else:
            self.hit_points = max(int(self.hit_points - damage), 0)

    def get_cursed(self):
        self.cursed = True

    def defeated(self):
        return self.hit_points == 0
    

class Monster():
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
            "heal" : "Restores " + str(self.healing) + " hit points",
            "power" : "Increases the monster's next attack by " + str(round((self.power_inc - 1) * 100)) + "%",
            "defend" : "Reduces the next damage the monster takes by " + str(round((1 - self.defense) * 100)) + "%",
            "curse" : "Prevents you from using or gaining magic on your next turn"
        }

        self.print_all_moves()

    # gameplay methods
    def print_stats(self):
        print("\nMonster Stats and Effects:")
        print("Monster Health: " + str(self.hit_points) + "/" + str(self.max_hit_points))
        if self.powered_up: print("The monster is powered up!")
        if self.defending: print("The monster is defending!")
    
    def print_all_moves(self):
        print("\nA new monster appeared! It has these moves!")
        for move in self.actions:
            print(move + ": " + self.actions[move])

    def get_available_moves(self, hero):
        moves = ["attack", "curse"]     # monster can always attack and curse
        if self.hit_points != self.max_hit_points:
            moves.append("heal")
        if not self.powered_up:
            moves.append("power")
        if not self.defending:
            moves.append("defend")
        return moves

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

    def play_turn(self, hero):
        moves = self.get_available_moves(hero)      # get list of available moves
        action = random.choice(moves)               # randomly pick next move
        print("The monster used " + action + "!")
        self.do_action(action, hero)                # do action

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

    def curse(self, hero):
        hero.get_cursed()

    # hero method effects
    def take_damage(self, damage):
        if self.defending:
            self.hit_points = max(int(self.hit_points - (damage * self.defense)), 0)
            self.defending = False
        else:
            self.hit_points = max(int(self.hit_points - damage), 0)

    def get_stunned(self):
        self.powered_up = False
        self.defending = False
    
    def defeated(self):
        return self.hit_points == 0

# initialize player, points, and enemy
hero = Player()
points = 0
enemy = Monster(points)

# start game loop
while not hero.defeated():
    hero.play_turn(enemy)
    if enemy.defeated():
        points += 1
        enemy = Monster(points)
    else:
        enemy.play_turn(hero)

print("Oh no! You died! You scored " + str(points) + " points!")