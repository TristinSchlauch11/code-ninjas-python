import random

class Player():
    def __init__(self):
        # health
        self.hit_points = 200
        self.max_hit_points = 200

        # magic
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
            "heal" : "Restores " + str(self.healing) + " HP",
            "power" : "Increases next attack by " + str(round((self.power_inc - 1) * 100)) + "%",
            "defend" : "Reduces the next damage taken by " + str(round((1 - self.defense) * 100)) + "%",
            "curse" : "You cannot use/gain magic on your next turn"
        }

    # gameplay methods
    def get_available_moves(self, hero):
        moves = ["attack", "curse"]     # monster can always attack and curse
        if self.hit_points != self.max_hit_points:
            moves.append("heal")
        if not self.powered_up:
            moves.append("power")
        if not self.defending:
            moves.append("defend")
        return moves

    def pick_move(self, hero):
        moves = self.get_available_moves(hero)      # get list of available moves
        return random.choice(moves)                 # randomly pick next move

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
