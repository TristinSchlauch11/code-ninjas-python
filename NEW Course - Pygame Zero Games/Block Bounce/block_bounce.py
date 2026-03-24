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

# sprite coordinate lists
square_coords = []
plat_coords = []
spike_coords = []
short_spike_coords = []
up_coords = []
down_coords = []
block_coords = []
rocket_coords = []
jumppad_coords = []

# mass sprite lists
platforms = []
spikes = []
mods = []

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

def create_obst(pos_list, image, kind):
    for (col, row, upside_down) in pos_list:
        # create the sprite and set its position
        sprite = Actor(image)
        sprite.left = 790 + 45*col
        if not upside_down:
            sprite.bottom = 135 + 45*row
        else:
            sprite.angle = 180
            sprite.top = 90 + 45*row
        # add it to the necessary list
        if kind == "plat":
            platforms.append(sprite)
        elif kind == "spike":
            spikes.append(sprite)
        elif kind == "mod":
            mods.append(sprite)

# create all sprites
create_obst(square_coords, "block", "plat")
create_obst(plat_coords, "platform", "plat")
create_obst(spike_coords, "spike", "spike")
create_obst(short_spike_coords, "short_spike", "spike")
create_obst(up_coords, "up_ring", "mod")
create_obst(down_coords, "down_ring", "mod")
create_obst(rocket_coords, "rocket_ring", "mod")
create_obst(block_coords, "block_ring", "mod")
create_obst(jumppad_coords, "jump_pad", "mod")

def draw():
    bg.draw()
    if won:
        screen.draw.text("YOU WIN", center = (screen.width / 2, screen.height / 2), fontsize = 72, color = (255, 255, 255))
    else:
        if not crashed:
            player.draw()
        for plat in platforms:
            plat.draw()
        for spike in spikes:
            spike.draw()
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

    # check for collision with platforms
    plat_index = player.collidelist(platforms)
    if plat_index != -1:
        plat = platforms[plat_index]
        # check if we ran into the platform
        if player.right < plat.left + 15:
            crash()
        # check if we have landed on the platform
        elif gravity == 1 and player.bottom < plat.top + 25:
            player.bottom = plat.top
            velocity = 0
            on_ground = True
        elif gravity == -1 and player.top > plat.bottom - 25:
            player.top = plat.bottom
            velocity = 0
            on_ground = True
        # we hit the platform in some other way
        else:
            crash()

    # check for collisions with spikes
    if player.collidelist(spikes) != -1:
        crash()

    # check for collision with mods
    mod_index = player.collidelist(mods)
    if mod_index != -1:
        mod = mods[mod_index]
        pass_mod(mod)

    # move all objects
    if not crashed:
        x_offset += 10
        for plat in platforms:
            plat.x -= 10
        for spike in spikes:
            spike.x -= 10
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
        reset()

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
        clock.schedule_unique(reset, 2.0)

def reset():
    global attempt
    global crashed
    global x_offset
    global form
    global gravity
    global velocity

    attempt += 1
    crashed = False

    # reset all obstacles
    for plat in platforms:
        plat.x += x_offset
    for spike in spikes:
        spike.x += x_offset
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
