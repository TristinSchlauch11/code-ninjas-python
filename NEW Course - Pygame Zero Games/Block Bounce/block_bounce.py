# screen dimensions
WIDTH = 1000
HEIGHT = 500

# game variables
on_ground = True
clicked = False
attempt = 1

x_offset = 0
form = "block"
crashed = False
won = False

# physics variables
gravity = 1
velocity = 0

# sprites
bg = Actor("background")
bg.bottomleft = (0, 600)

player = Actor("player_block")
player.bottomleft = (200, 450)

# sprite lists
square_coords = []
plat_coords = []
spike_coords = []
short_spike_coords = []
up_coords = []
down_coords = []
block_coords = []
rocket_coords = []
jumppad_coords = []

file = open("encoded_tilemap.txt", "r")
for i, line in enumerate(file.readlines()):
    for j, char in enumerate(line):
        if char == "1":
            square_coords.append((j, i, False))
        elif char == "2":
            plat_coords.append((j, i, True))
        elif char == "3":
            plat_coords.append((j, i, False))
        elif char == "a":
            spike_coords.append((j, i, False))
        elif char == "b":
            short_spike_coords.append((j, i, False))
        elif char == "c":
            spike_coords.append((j, i, True))
        elif char == "d":
            short_spike_coords.append((j, i, True))
        elif char == "w":
            rocket_coords.append((j, i, False))
        elif char == "x":
            block_coords.append((j, i, False))
        elif char == "y":
            up_coords.append((j, i, False))
        elif char == "z":
            down_coords.append((j, i, False))
        elif char == "@":
            jumppad_coords.append((j, i, False))
        elif char == "#":
            jumppad_coords.append((j, i, True))
file.close()

# spike and platform sprites
def create_obst(pos_list, image, can_land):
    for (col, row, upside_down) in pos_list:
        # create the sprite and set its position
        sprite = Actor(image)
        sprite.left = 700 + 45*col
        if not upside_down:
            sprite.bottom = 135 + 45*row
        else:
            sprite.angle = 180
            sprite.top = 90 + 45*row
        # add it to the neccesary lists
        all_obst.append(sprite)
        if can_land:
            platforms.append(sprite)

# ring and jumppad sprites
def create_mod(pos_list, image):
    for (col, row, upside_down) in pos_list:
        # create the sprite and set its position
        sprite = Actor(image)
        sprite.left = 700 + 45*col
        if not upside_down:
            sprite.bottom = 135 + 45*row
        else:
            sprite.angle = 180
            sprite.top = 90 + 45*row
        # add it to the neccesary lists
        mods.append(sprite)

# mass sprite lists
platforms = []
all_obst = []
mods = []

# create all other sprites
create_obst(square_coords, "block", True)
create_obst(plat_coords, "platform", True)
create_obst(spike_coords, "spike", False)
create_obst(short_spike_coords, "short_spike", False)
create_mod(up_coords, "up_ring")
create_mod(down_coords, "down_ring")
create_mod(rocket_coords, "rocket_ring")
create_mod(block_coords, "block_ring")
create_mod(jumppad_coords, "jump_pad")

def draw():
    bg.draw()
    if won:
        screen.draw.text("YOU WIN", center = (screen.width / 2, screen.height / 2), fontsize = 72, color = (255, 255, 255))

    else:
        if not crashed:
            player.draw()

        for obst in all_obst:
            obst.draw()

        for mod in mods:
            mod.draw()

        screen.draw.text("Attempt " + str(attempt), midleft = (800 - x_offset, 100), fontsize = 64, color = (255, 255, 255))

def update():
    global velocity
    global x_offset
    global crashed
    global on_ground
    global won

    # player movement
    if form == "block":
        if (keyboard.space or clicked) and on_ground:
            velocity = -15*gravity
        elif velocity < 25 and velocity > -25:
            velocity += gravity
        on_ground = False       # to prevent mid-air jumps
    elif form == "rocket":
        if (keyboard.space or clicked):
            velocity += -0.5*gravity
        else:
            velocity += 0.5*gravity

    player.y += velocity

    # check if the player is on the floor
    if player.bottom > 450:
        player.bottom = 450
        velocity = 0
        on_ground = True


    # check if player has collided with roof
    if player.top < 0:
        # if as rocket
        if form == "rocket":
            player.top = 0
            velocity = 0
        # if as gravity inverted:
        if gravity == -1:
            crash()

    # check for collision with obstacles
    o_index = player.collidelist(all_obst)
    if o_index != -1:
        obstacle = all_obst[o_index]
        # check if we hit a spike
        if obstacle not in platforms:
            crash()
        else:
            # check if we ran into a platform
            if player.right < obstacle.left + 15:
                crash()
            # check if we have landed on a platform
            elif gravity == 1 and player.bottom < obstacle.top + 25:
                player.bottom = obstacle.top
                velocity = 0
                on_ground = True
            elif gravity == -1 and player.top > obstacle.bottom - 25:
                player.top = obstacle.bottom
                velocity = 0
                on_ground = True
            # we hit the platform in some other way
            else:
                crash()

    # check for collision with mods
    mod_index = player.collidelist(mods)
    if mod_index != -1:
        mod = mods[mod_index]
        pass_mod(mod)

    # move all other stuff
    if not crashed:
        x_offset += 10
        for obst in all_obst:
            obst.x -= 10
        for mod in mods:
            mod.x -= 10

    # check if the player won
    if x_offset >= 3000:
        won = True

def on_mouse_down(button):
    global clicked
    if button == mouse.LEFT:
        clicked = True

def on_mouse_up(button):
    global clicked
    if button == mouse.LEFT:
        clicked = False

def on_key_down(key):
    if key == keys.RETURN:
        reset_all_obst()

def pass_mod(mod):
    global gravity
    global velocity
    global form

    if mod.image == "down_ring":
        gravity = 1
    elif mod.image == "up_ring":
        gravity = -1

    if mod.image == "block_ring":
        player.image = "player_block"
        form = "block"
    elif mod.image == "rocket_ring":
        player.image = "player_rocket"
        form = "rocket"

    if mod.image == "jump_pad":
        velocity = -24*gravity

def crash():
    global crashed

    if not crashed:
        crashed = True
        clock.schedule_unique(reset_all_obst, 2.0)

def reset_all_obst():
    global attempt
    global crashed
    global x_offset
    global form
    global gravity
    global velocity

    attempt += 1
    crashed = False

    # reset all obstacles
    for obst in all_obst:
        obst.x += x_offset
    for mod in mods:
        mod.x += x_offset

    # reset player
    form = "block"
    player.image = "player_block"
    player.bottomleft = (200, 450)
    gravity = 1
    velocity = 0

    # reset offset
    x_offset = 0
