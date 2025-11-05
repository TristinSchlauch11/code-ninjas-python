from pgzhelper import *
from dungeon_fighter_game import *

# game variables
WIDTH = 800
HEIGHT = 600

slain = 0
is_your_turn = True
game_over = False
message = "A Level " + str(slain + 1) + " monster appeared!"

# background
background = Actor("background")
background.topleft = (0,-150)

# player and enemy objects
player = Player()
enemy = Monster(slain)

# player wizard sprite
wizard = Actor("wizard_idle0")
wizard.center = (235, 175)

# wizard animation
wizard_idle = ["wizard_idle0", "wizard_idle1", "wizard_idle2", "wizard_idle3", "wizard_idle4"]
wizard_action = ["wizard_attack0", "wizard_attack1", "wizard_attack2", "wizard_attack3", "wizard_attack4", "wizard_attack5", "wizard_attack6", "wizard_attack7", "wizard_attack8", "wizard_attack9"]
wizard_hurt = ["wizard_hurt0", "wizard_hurt1", "wizard_hurt2", "wizard_hurt3", "wizard_hurt4"]
wizard_death = ["wizard_death0", "wizard_death1", "wizard_death2", "wizard_death3", "wizard_death4", "wizard_death5", "wizard_death6", "wizard_death7", "wizard_death8", "wizard_death9", "wizard_death10", "wizard_death11"]
wizard.images = wizard_idle
wizard.fps = 10

# enemy wraith sprite
wraith = Actor("wraith_idle0")
wraith.center = (550, 200)

# wraith animation
wraith_idle = ["wraith_idle0", "wraith_idle1", "wraith_idle2", "wraith_idle3", "wraith_idle4", "wraith_idle5", "wraith_idle6", "wraith_idle7", "wraith_idle8", "wraith_idle9", "wraith_idle10", "wraith_idle11"]
wraith_action = ["wraith_attack0", "wraith_attack1", "wraith_attack2", "wraith_attack3", "wraith_attack4", "wraith_attack5", "wraith_attack6", "wraith_attack7", "wraith_attack8", "wraith_attack9", "wraith_attack10", "wraith_attack11"]
wraith_hurt = ["wraith_hurt0", "wraith_hurt1", "wraith_hurt2", "wraith_hurt3", "wraith_hurt4", "wraith_hurt5", "wraith_hurt6", "wraith_hurt7", "wraith_hurt8", "wraith_hurt9", "wraith_hurt10", "wraith_hurt11"]
wraith_death = ["wraith_death0", "wraith_death1", "wraith_death2", "wraith_death3", "wraith_death4", "wraith_death5", "wraith_death6", "wraith_death7", "wraith_death8", "wraith_death9", "wraith_death10", "wraith_death11", "wraith_death12", "wraith_death13", "wraith_death14"]
wraith.images = wraith_idle
wraith.fps = 10

# modifier icons
player_power = Actor("powerup")
player_power.topleft = (12, 55)
player_defence = Actor("sheild")
player_defence.topleft = (52, 55)

enemy_power = Actor("powerup")
enemy_power.topright = (788, 55)
enemy_defence = Actor("sheild")
enemy_defence.topright = (748, 55)

# button information for player - list of dictionaries
texts = ["Attack", "Summon", "Heal", "Power Up", "Defend", "Stun"]
actions = ["attack", "magic", "heal", "power", "defend", "stun"]
button_info = []
for i in range(6):
    button_info.append({"text" : texts[i], "action" : actions[i], "rect" : Rect(30, 310 + i * 45, 100, 35)})

# monster move list
monster_texts = ["Attack", "Heal", "Power Up", "Defend", "Curse"]
monster_actions = ["attack", "heal", "power", "defend", "curse"]

def draw():

    screen.fill((22,22,22))
    background.draw()

    if game_over:
        screen.draw.text("Oh no, you died!", center = (WIDTH / 2, 275), fontsize = 36, color = (255, 255, 255))
        screen.draw.text("You slayed " + str(slain) + " monsters!", center = (WIDTH / 2, 325), fontsize = 36, color = (255, 255, 255))
    else:
        # draw wizard
        wizard.draw()
        wizard.scale = 0.5

        # draw wraith
        wraith.draw()
        wraith.scale = 0.5

        # draw health/magic bars
        # player health
        screen.draw.rect(Rect((12, 12, 206, 16)), color = (255, 255, 255))
        screen.draw.filled_rect(Rect(15, 15, player.hit_points, 10), color = (255, 0, 0))
        screen.draw.text("HP: " + str(player.hit_points), topleft = (225, 15), color = (255, 255, 255), fontsize = 16)

        # player magic
        screen.draw.rect(Rect((12, 32, 206, 16)), color = (255, 255, 255))
        screen.draw.filled_rect(Rect(15, 35, player.magic, 10), color = (5, 191, 242))
        screen.draw.text("MP: " + str(player.magic), topleft = (225, 35), color = (255, 255, 255), fontsize = 16)

        # enemy health
        screen.draw.rect(Rect((582, 12, 206, 16)), color = (255, 255, 255))
        screen.draw.filled_rect(Rect(785 - (enemy.hit_points / enemy.max_hit_points * 200), 15, enemy.hit_points / enemy.max_hit_points * 200, 10), color = (255, 0, 0))
        screen.draw.text("HP: " + str(enemy.hit_points), topright = (575, 15), color = (255, 255, 255), fontsize = 16)

        # draw modifier icons
        if player.powered_up:
            player_power.draw()
        if player.defending:
            player_defence.draw()
        if enemy.powered_up:
            enemy_power.draw()
        if enemy.defending:
            enemy_defence.draw()

        # draw selection buttons
        # player options
        screen.draw.filled_rect(Rect(20, 300, 370, 280), color = (100, 100, 100))
        for i in range(6):
            button = button_info[i]
            if button["action"] in player.get_available_moves(enemy) and is_your_turn:
                screen.draw.filled_rect(button["rect"], color = (60, 50, 50))
                screen.draw.text(button["text"], center = button["rect"].center, color = (250, 155, 25))
                screen.draw.text(player.actions[button["action"]], midleft = (135, 328 + 45 * i), color = (255, 255, 255), fontsize = 16)
            else:
                screen.draw.filled_rect(button["rect"], color = (30, 20, 20))
                screen.draw.text(button["text"], center = button["rect"].center, color = (125, 80, 20))
                screen.draw.text(player.actions[button["action"]], midleft = (135, 328 + 45 * i), color = (50, 50, 50), fontsize = 16)

        # monster options
        screen.draw.filled_rect(Rect(410, 300, 370, 235), color = (100, 100, 100))
        for j in range(5):
                action = monster_actions[j]
                option_rect = Rect(670, 310 + j * 45, 100, 35)
                if action in enemy.get_available_moves(player) and not is_your_turn:
                    screen.draw.filled_rect(option_rect, color = (60, 50, 50))
                    screen.draw.text(monster_texts[j], center = option_rect.center, color = (10, 230, 160))
                    screen.draw.text(enemy.actions[action], midright = (665, 328 + 45 * j), color = (255, 255, 255), fontsize = 16)
                else:
                    screen.draw.filled_rect(option_rect, color = (30, 20, 20))
                    screen.draw.text(monster_texts[j], center = option_rect.center, color = (10, 100, 70))
                    screen.draw.text(enemy.actions[action], midright = (665, 328 + 45 * j), color = (50, 50, 50), fontsize = 16)

        # draw last action to the screen
        screen.draw.text(message, center = (595, 565), color = (255, 255, 255), fontsize = 28)

def update():
    wizard.animate()
    wraith.animate()

def on_mouse_down(pos, button):
    global is_your_turn

    # check if you clicked a button and that it's your turn
    if button == mouse.LEFT and is_your_turn:
        for option in button_info:
            action = option["action"]
            if option["rect"].collidepoint(pos) and action in player.get_available_moves(enemy):

                # perform action
                wizard_action_anim(action)
                player.do_action(action, enemy)

                # check if monster died as a result of your action
                if enemy.defeated():
                    is_your_turn = False
                    clock.schedule_unique(wraith_death_anim, 2.0)
                    clock.schedule_unique(spawn_new_monster, 3.5)

                # if not, make it monster's turn
                elif action != "stun":
                    is_your_turn = False
                    clock.schedule_unique(play_monster_turn, 2.5)

def spawn_new_monster():
    global slain
    global enemy
    global message

    slain += 1
    enemy = Monster(slain)
    message = "A Level " + str(slain + 1) + " monster appeared!"
    clock.schedule_unique(start_your_turn, 0.5)

def play_monster_turn():
    global message

    # perform action
    action = enemy.pick_move(player)
    message = "The monster used " + monster_texts[monster_actions.index(action)] + "!"
    wraith_action_anim(action)
    enemy.do_action(action, player)

    # check if you died as a result of the monsters actions
    if player.defeated():
        # end game
        clock.schedule_unique(wizard_death_anim, 1.4)
        clock.schedule_unique(end_game, 2.4)
    else:
        # otherwise, start your next turn
        clock.schedule_unique(start_your_turn, 2.0)

def start_your_turn():
    global is_your_turn
    is_your_turn = True

def wizard_action_anim(action):
    wizard.center = (305, 175)
    wizard.images = wizard_action
    if action == "attack" or action == "stun":
        clock.schedule_unique(wraith_hurt_anim, 0.4)
    clock.schedule_unique(reset_wizard_anim, 1.0)

def wizard_hurt_anim():
    wizard.images = wizard_hurt
    clock.schedule_unique(reset_wizard_anim, 0.4)

def wizard_death_anim():
    wizard.images = wizard_death

def reset_wizard_anim():
    wizard.center = (235, 175)
    wizard.images = wizard_idle

def wraith_action_anim(action):
    wraith.images = wraith_action
    if action == "attack" or action == "curse":
        clock.schedule_unique(wizard_hurt_anim, 0.8)
    clock.schedule_unique(reset_wraith_anim, 1.1)

def wraith_hurt_anim():
    wraith.images = wraith_hurt
    clock.schedule_unique(reset_wraith_anim, 1.1)

def wraith_death_anim():
    wraith.images = wraith_death
    clock.schedule_unique(reset_wraith_anim, 1.4)

def reset_wraith_anim():
    wraith.images = wraith_idle

def end_game():
    global game_over
    game_over = True
    background.topleft = (0,0)
